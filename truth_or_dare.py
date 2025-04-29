import random
import time

# Truth और Dare की लिस्ट
truths = [
    "😜 तुम्हारा सबसे गहरा राज क्या है?",
    "🙈 तुम्हें अब तक का सबसे शर्मनाक पल कौन सा लगा?",
    "😏 क्या तुमने कभी किसी को झूठ बोलकर फंसाया है?",
    "💘 किसी पर अभी भी क्रश है क्या?",
    "🕵️ क्या तुमने कभी किसी की चीज़ चुराई है?"
]

dares = [
    "🕺 10 सेकंड का फनी डांस करो (कैमरा ऑन हो तो मज़ा दोगुना!)",
    "📞 किसी को कॉल करो और बोलो 'I love you ❤️'",
    "🐴 5 बार ऊँची आवाज़ में बोलो 'मैं गधा हूँ!'",
    "🎤 बिना रुके 1 मिनट तक कोई भी गाना गाओ!",
    "🤪 अपना सबसे अजीब चेहरा बनाओ और उसका सेल्फ़ी लो!"
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
