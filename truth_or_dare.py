import random
import time

# Truth और Dare की लिस्ट
truths = [
    "What is one goal you’ve set for yourself this year and how close are you to achieving it?",
    "What is something you’ve never told anyone, but you wish you could share?",
    "Have you ever had a major turning point in your life that changed you permanently?",
    "If you could switch lives with anyone for a day, who would it be and why?",
    "What’s the biggest risk you’ve ever taken, and did it pay off?"
]


dares = [
    "Perform a 30-second motivational speech like you're addressing a crowd at a TED Talk.",
    "Pretend you are a news anchor and deliver a funny news segment for 60 seconds.",
    "Act like your favorite celebrity for the next 2 minutes, and let others guess who you’re impersonating.",
    "Read a passage from a book or article in a dramatic fashion like you’re in a movie scene.",
    "For the next 3 minutes, speak in an accent of your choice and don’t break character!"
]


def loading_animation(text="सोच रहा हूँ..."):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(0.05)
    print("\n")

def play_game():
    print("🎉✨ Welcome to the Ultimate Truth or Dare Game! ✨🎉")
    print("👉 Type 'exit' anytime to leave the game.\n")

    while True:
        player = input("👤 Enter player name (or type 'exit' to quit): ").strip()
        if player.lower() == 'exit':
            print("🙏 धन्यवाद! फिर मिलेंगे एक और मज़ेदार Truth or Dare में!")
            break

        choice = input(f"\n{player}, choose wisely... Truth (T) or Dare (D)? ").lower()
        print()

        if choice == 't':
            loading_animation("सच सामने लाया जा रहा है...")
            print("🟢 Your TRUTH:", random.choice(truths))
        elif choice == 'd':
            loading_animation("डरावनी चुनौती चुनी जा रही है...")
            print("🔴 Your DARE:", random.choice(dares))
        else:
            print("❌ Invalid choice! Please type 'T' for Truth or 'D' for Dare.\n")

        print("-" * 50 + "\n")

# Run the game
if __name__ == "__main__":
    play_game()
