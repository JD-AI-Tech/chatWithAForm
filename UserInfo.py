from pydantic import BaseModel, Field

class PersonalDetails(BaseModel):
    first_name: str = Field(
        ...,
        description="This is the first name of the user.",
    )
    last_name: str = Field(
        ...,
        description="This is the last name or surname of the user.",
    )
    company: str = Field(
        ...,
        description="This is the company where user works, or previously worked for.",
    )
    topic: str = Field(
        ...,
        description="Is the issue, topic, item of interest or the information the user is requesting ",
    )
    email: str = Field(
        ...,
        description="an email address that the person associates as theirs",
    )
    job_title: str = Field(
        ...,
        description="the job title, job description, position, or the profession title of the user",
    )
    language: str = Field(
        ..., enum=["spanish", "english", "french", "german", "italian"]
    )