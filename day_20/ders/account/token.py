from django.contrib.auth.tokens import PasswordResetTokenGenerator

class UserVerificationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        user_id = str(user.pk)
        ts = str(timestamp)
        is_active = str(user.is_active)
        return f"{user_id}{ts}{is_active}"
    
user_tokenizer_generate = UserVerificationTokenGenerator()