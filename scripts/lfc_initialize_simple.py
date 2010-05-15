# django imports
from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType

# lfc imports
from lfc.models import Portal
from lfc.models import Page
from lfc.models import WorkflowStatesInformation

# portlets import
from portlets.models import Slot

# workflows import
import workflows.utils
from workflows.models import State
from workflows.models import StateInheritanceBlock
from workflows.models import Transition
from workflows.models import Workflow
from workflows.models import WorkflowPermissionRelation

# permissions imports
import permissions.utils

# scripts imports
from lfc.utils.initialize import initialize

def load_data():
    """This will create default portlets, templates and content types, simple
    Roles and a simple workflow (just private and public).
    
    This can be used for small sites without different roles.
    """
    # Register default portlets, templates and content types.
    initialize()

    # Register site
    site = Site.objects.all()[0]
    site.name = site.domain = "www.example.com"
    site.save()
    
    # Create portal
    portal = Portal.objects.create()

    # Register roles
    anonymous = permissions.utils.register_role("Anonymous")

    # Registers permissions
    view = permissions.utils.register_permission("View", "view")

    # Create slots
    left_slot, created = Slot.objects.get_or_create(name="Left")
    right_slot, created = Slot.objects.get_or_create(name="Right")

    # Set permissions for portal
    permissions.utils.grant_permission(portal, anonymous, "view")

    # Simple Workflow
    ##########################################################################

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

    # Add all permissions which are managed by the workflow
    WorkflowPermissionRelation.objects.create(workflow=workflow, permission=view)

    # Add permissions for single states
    # Private
    StateInheritanceBlock.objects.create(state=private, permission=view)

    # Define public state
    WorkflowStatesInformation.objects.create(state=public, public=True)

    # Define initial state
    workflow.initial_state = private
    workflow.save()

    # Set workflow for Page
    ctype = ContentType.objects.get_for_model(Page)
    workflows.utils.set_workflow_for_model(ctype, workflow)

def run():
    load_data()