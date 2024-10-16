

class VkUserSchema:
    user_id: int | None = None
    name: str | None = None
    surname: str | None = None
    age: int | None = None
    city: str | None = None
    posts: list | None = None
    groups: list | None = None
    subscriptions: list | None = None

    @classmethod
    def add(
            cls, user_id: int, name: str, surname: str, age: int, city: str, posts: list, groups: list, subscriptions: list
    ) -> None:
        cls.user_id = user_id
        cls.name = name
        cls.surname = surname
        cls.age = age
        cls.city = city
        cls.posts = posts
        cls.groups = groups
        cls.subscriptions = subscriptions

    @classmethod
    def clear(cls) -> None:
        cls.user_id = None
        cls.name = None
        cls.surname = None
        cls.age = None
        cls.city = None
        cls.posts = None
        cls.groups = None
        cls.subscriptions = None

    def __repr__(self) -> str:
        candidate = (f"Candidate(\n"
                     f"user_id={self.user_id!r}"
                     f"name={self.name!r}\n"
                     f"surname={self.surname!r}\n"
                     f"age={self.age!r}\n"
                     f"city={self.city!r}\n"
                     f"posts={self.posts!r}\n"
                     f"groups={self.groups!r}\n"
                     f"subscriptions={self.subscriptions!r}\n"
                     f")")
        return candidate
