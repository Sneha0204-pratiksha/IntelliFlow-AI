from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.workflow import Workflow
from app.schemas.workflow import WorkflowCreate, WorkflowUpdate

router = APIRouter()


# Create Workflow
@router.post("/")
def create_workflow(
    workflow: WorkflowCreate,
    db: Session = Depends(get_db)
):
    new_workflow = Workflow(
        title=workflow.title,
        description=workflow.description,
        created_by=workflow.created_by
    )

    db.add(new_workflow)
    db.commit()
    db.refresh(new_workflow)

    return {
        "message": "Workflow Created Successfully",
        "workflow_id": new_workflow.id
    }


# Get All Workflows
@router.get("/")
def get_workflows(db: Session = Depends(get_db)):
    return db.query(Workflow).all()


# Get Workflow by ID
@router.get("/{workflow_id}")
def get_workflow(
    workflow_id: int,
    db: Session = Depends(get_db)
):
    workflow = db.query(Workflow).filter(
        Workflow.id == workflow_id
    ).first()

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    return workflow


# Update Workflow
@router.put("/{workflow_id}")
def update_workflow(
    workflow_id: int,
    workflow: WorkflowUpdate,
    db: Session = Depends(get_db)
):
    db_workflow = db.query(Workflow).filter(
        Workflow.id == workflow_id
    ).first()

    if db_workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    db_workflow.title = workflow.title
    db_workflow.description = workflow.description
    db_workflow.status = workflow.status

    db.commit()
    db.refresh(db_workflow)

    return {
        "message": "Workflow Updated Successfully"
    }


# Delete Workflow
@router.delete("/{workflow_id}")
def delete_workflow(
    workflow_id: int,
    db: Session = Depends(get_db)
):
    workflow = db.query(Workflow).filter(
        Workflow.id == workflow_id
    ).first()

    if workflow is None:
        raise HTTPException(
            status_code=404,
            detail="Workflow not found"
        )

    db.delete(workflow)
    db.commit()

    return {
        "message": "Workflow Deleted Successfully"
    }