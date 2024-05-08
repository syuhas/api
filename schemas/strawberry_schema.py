import typing
import strawberry
from scalars.user_scalar import StrawberryUser, StrawberryUserMutation, TestQuery
from resolvers.resolver import listusers, newUser


@strawberry.type
class Query:
    @strawberry.field
    async def users(self) -> typing.List[TestQuery]:
        userlist = await listusers()
        return userlist
    

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def addANewUser(
        self,
        username: str,
        pw: str = None,
        email: str = None,
        firstname: str = None,
        lastname: str = None,
        phone: str = None,
        linkedin: str = None,
        confirmed: bool = None,
        profile_link: str = None,
        date_created: str = None
    ) -> typing.List[TestQuery]:
        await newUser(
            username=username,
            pw=pw,
            email=email,
            firstname=firstname,
            lastname=lastname,
            phone=phone,
            linkedin=linkedin,
            confirmed=confirmed,
            profile_link=profile_link,
            date_created=date_created
        )
        new_db_user = await listusers()
        return new_db_user
    

