"""Login to Garmin once (supports MFA) and save token to token.txt."""
import getpass

from garminconnect import Garmin

email = input("Garmin email: ").strip()
password = getpass.getpass("Garmin password: ")

garmin = Garmin(email=email, password=password, return_on_mfa=True)
result1, result2 = garmin.login()
if result1 == "needs_mfa":
    mfa = input("MFA code (from email/app): ").strip()
    garmin.resume_login(result2, mfa)

store = getattr(garmin, "client", None) or garmin.garth
with open("token.txt", "w") as f:
    f.write(store.dumps())
print("\nOK - token saved to token.txt")
