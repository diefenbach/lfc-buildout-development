# python imports
import os

# django imports
from django.conf import settings
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.template.defaultfilters import slugify
from django.contrib.webdesign.lorem_ipsum import paragraph, sentence, words

# lfc imports
from lfc.models import Portal
from lfc.models import Page

# portlets import
from portlets.models import Slot

# workflows import
import workflows.utils
from workflows.models import State
from workflows.models import StateInheritanceBlock
from workflows.models import StatePermissionRelation
from workflows.models import Transition
from workflows.models import Workflow
from workflows.models import WorkflowPermissionRelation

# permissions imports
import permissions.utils

def load_data():

    site = Site.objects.all()[0]
    site.name = site.domain = "www.example.com"
    site.save()

    portal = Portal.objects.create()

    # Add workflow
    workflow, created = Workflow.objects.get_or_create(name="Simple")

    # Add states
    private = State.objects.create(name="Private", workflow=workflow)
    public = State.objects.create(name="Public", workflow=workflow)

    # Create transitions
    make_public = Transition.objects.create(name="Make public", workflow=workflow, destination = public)
    make_private = Transition.objects.create(name="Make private", workflow=workflow, destination = private)

    # Add transitions
    private.transitions.add(make_public)
    public.transitions.add(make_private)

    # Register groups
    anonymous = permissions.utils.register_group("Anonymous")
    manager = permissions.utils.register_group("Manager")
    owner = permissions.utils.register_group("Owner")

    # Registers permissions
    add = permissions.utils.register_permission("Add", "add")
    delete = permissions.utils.register_permission("Delete", "delete")
    edit = permissions.utils.register_permission("Edit", "edit")
    view = permissions.utils.register_permission("View", "view")

    ctype = ContentType.objects.get_for_model(Portal)
    manage_portal = permissions.utils.register_permission("Manage Portal", "manage_portal", [ctype])

    # Add all permissions which are managed by the workflow
    WorkflowPermissionRelation.objects.create(workflow=workflow, permission=add)
    WorkflowPermissionRelation.objects.create(workflow=workflow, permission=delete)
    WorkflowPermissionRelation.objects.create(workflow=workflow, permission=edit)
    WorkflowPermissionRelation.objects.create(workflow=workflow, permission=view)

    # Add permissions for single states
    StatePermissionRelation.objects.create(state=private, permission=add, group=owner)
    StatePermissionRelation.objects.create(state=private, permission=delete, group=owner)
    StatePermissionRelation.objects.create(state=private, permission=edit, group=owner)
    StatePermissionRelation.objects.create(state=private, permission=view, group=owner)

    StatePermissionRelation.objects.create(state=private, permission=add, group=manager)
    StatePermissionRelation.objects.create(state=private, permission=delete, group=manager)
    StatePermissionRelation.objects.create(state=private, permission=edit, group=manager)
    StatePermissionRelation.objects.create(state=private, permission=view, group=manager)

    # Add inheritance block for single states
    StateInheritanceBlock.objects.create(state=private, permission=add)
    StateInheritanceBlock.objects.create(state=private, permission=delete)
    StateInheritanceBlock.objects.create(state=private, permission=edit)
    StateInheritanceBlock.objects.create(state=private, permission=view)

    StateInheritanceBlock.objects.create(state=public, permission=add)
    StateInheritanceBlock.objects.create(state=public, permission=delete)
    StateInheritanceBlock.objects.create(state=public, permission=edit)

    # Define initial state
    workflow.initial_state = private
    workflow.save()

    # Set workflow for Page
    ctype = ContentType.objects.get_for_model(Page)
    workflows.utils.set_workflow_for_model(ctype, workflow)

    # Create slots
    left_slot, created = Slot.objects.get_or_create(name="Left")
    right_slot, created = Slot.objects.get_or_create(name="Right")

    # Set permissions for portal
    permissions.utils.grant_permission(portal, "add", manager)
    permissions.utils.grant_permission(portal, "delete", manager)
    permissions.utils.grant_permission(portal, "edit", manager)
    permissions.utils.grant_permission(portal, "manage_portal", manager)
    permissions.utils.grant_permission(portal, "view", manager)

    permissions.utils.grant_permission(portal, "view", anonymous)
    permissions.utils.grant_permission(portal, "view", owner)


def run():
    load_data()


