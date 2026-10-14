import time
import token_bucket_two
from token_bucket_two import TokenBucket


def test_token_bucket():
    # Capacity of 5 tokens, refills at 1 token per second
    bucket = TokenBucket(capacity=5, fill_rate=1)

    print(f"Initial tokens: {bucket.tokens}")

    print("\n--- 1. Consuming 3 tokens ---")
    if bucket.consume(3):
        print(f"Success! Remaining tokens: {bucket.tokens:.2f}")
    else:
        print("Failed to consume 3 tokens.")

    print("\n--- 2. Consuming 3 more tokens (Should fail, only 2 left) ---")
    if bucket.consume(3):
        print(f"Success! Remaining tokens: {bucket.tokens:.2f}")
    else:
        print(
            f"Failed as expected! Not enough tokens. Remaining: {bucket.tokens:.2f}"
        )

    print("\n--- 3. Consuming exact remaining 2 tokens ---")
    if bucket.consume(2):
        print(f"Success! Remaining tokens: {bucket.tokens:.2f}")
    else:
        print("Failed to consume 2 tokens.")

    print("\n--- 4. Waiting 2 seconds to let the bucket refill... ---")
    time.sleep(2)

    print("\n--- 5. Consuming 2 tokens after refill ---")
    if bucket.consume(2):
        print(f"Success! Tokens after consume: {bucket.tokens:.2f}")
    else:
        print("Failed to consume after waiting.")


if __name__ == "__main__":
    test_token_bucket()