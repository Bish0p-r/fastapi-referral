from fastapi import HTTPException, status

NonUniqueEmailOrUsernameException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="user with this email or username already exists",
)

ReferralTokenNotFoundException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="referral token not found",
)

InvalidUsernameException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid username",
)

InvalidPasswordException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid password",
)

ExpiredTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="expired token",
)

InvalidTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="invalid token",
)


NonUniqueReferralTokenException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="referral token already exists",
)

ReferralTokenAlreadyExistsException = HTTPException(
    status_code=status.HTTP_409_CONFLICT,
    detail="referral token already exists",
)

ReferralTokenDoesNotExistException = HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail="referral token does not exist",
)
