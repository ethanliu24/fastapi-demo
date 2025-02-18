from fastapi import APIRouter, Depends, HTTPException, status
from ...models.authentication import StandardUserSignUp
from ...services.auth import AuthenticationServices
from ...config.dependencies import get_auth_services

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login():
    pass


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def login(
    user_signup_model: StandardUserSignUp,
    auth_services: AuthenticationServices = Depends(get_auth_services)
):
    try:
        return await auth_services.signup(user_signup_model)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
