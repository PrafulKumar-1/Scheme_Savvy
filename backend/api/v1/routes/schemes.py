# FILE: backend/api/v1/routes/schemes.py
from fastapi import APIRouter, Depends
from typing import List
from backend.api.v1.schemas.scheme_schemas import UserProfile, Scheme
from backend.services.matching_service import matching_service, MatchingService

router = APIRouter()

@router.post("/find-schemes", response_model=List[Scheme])
def find_schemes_route(profile: UserProfile, service: MatchingService = Depends(lambda: matching_service)):
    """
    Receives user profile, uses the MatchingService to find eligible schemes,
    and returns a list of them.
    """
    return service.find_matching_schemes(profile)