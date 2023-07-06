import os
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.conf import settings
from infos import models


class Command(BaseCommand):
    help = "Creates an Consuming Application user non-interactively if it doesn't exist"

    def add_arguments(self, parser):
        parser.add_argument(
            "--client_id",
            help="The Client ID",
            default="9qGqxUYVcNrQyXgAWAu544YmAlBhmuZvtCqfKHap",
        )
        parser.add_argument(
            "--redirect", help="Redirect URIS", default="http://localhost"
        )
        parser.add_argument(
            "--client_secret",
            help="The Client Secret",
            default="MDmIMd3M5JamGqa7xBfF5oXFVELKclAJ4uG9ZHUrNH9XGDxggzbdYcv8ItJyjq4yiVMKPcK8seEdGrUnjKYNIdjqxUDceYXq9fznEr5F5ynXPu1IghHbFm3MbVScirJq",
        )

    def handle(self, *args, **options):
        apps = settings.ENSURED_APPS or []

        for app in apps:
            tenant = get_user_model().objects.get(username=app["TENANT"])

            manifest = models.Manifest(
                identifier=app["IDENTIFIER"],
                version=app["VERSION"],
                scopes=app["SCOPES"],
                redirect_uris=app["REDIRECT_URIS"],

            )

            if app["GRANT_TYPE"] == "client-credentials":
                models.create_private_client(
                    manifest,
                    tenant,
                    tenant,
                    client_id=app["CLIENT_ID"],
                    client_secret=app["CLIENT_SECRET"],
                    token=app["TOKEN"],
                )
            else:
                models.create_public_client(
                    manifest,
                    tenant,
                    client_id=app["CLIENT_ID"],
                    client_secret=app["CLIENT_SECRET"],
                    token=app["TOKEN"],
                )
