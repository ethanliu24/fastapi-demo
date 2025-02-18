from fastapi import APIRouter, Depends, HTTPException, status
from ...models.authentication import StandardUserSignUp, StandardUserLogin, JWTToken
from ...services.auth import AuthenticationServices
from ...config.dependencies import get_auth_services
from ...utils.utils import create_token_data

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/login")
async def login(
    login_data: StandardUserLogin,
    auth_services: AuthenticationServices = Depends(get_auth_services)
) -> JWTToken:
    user = await auth_services.authenticate_user(login_data)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return auth_services.generate_token(data=create_token_data(user.id))


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def login(
    user_signup_model: StandardUserSignUp,
    auth_services: AuthenticationServices = Depends(get_auth_services)
) -> JWTToken:
    try:
        return await auth_services.signup(user_signup_model)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
