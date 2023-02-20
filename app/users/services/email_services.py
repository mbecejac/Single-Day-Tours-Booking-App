import asyncio

from fastapi_mail import ConnectionConfig, FastMail, MessageSchema, MessageType
from pydantic import EmailStr

from app.config import settings


class EmailService:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.MAIL_USERNAME,
        MAIL_PASSWORD=settings.MAIL_PASSWORD,
        MAIL_PORT=settings.MAIL_PORT,
        MAIL_SERVER=settings.MAIL_SERVER,
        MAIL_FROM=settings.MAIL_FROM,
        MAIL_STARTTLS=False,
        MAIL_SSL_TLS=False,
    )

    @staticmethod
    def send_email_after_user_is_create(email: EmailStr):
        html = """<p> Dear User,<br> Welcome.</p>"""

        message = MessageSchema(
            subject="Welcome new user",
            recipients=[email],
            body=html,
            subtype=MessageType.html,
        )

        fm = FastMail(EmailService.conf)
        asyncio.run(fm.send_message(message))

        return True
