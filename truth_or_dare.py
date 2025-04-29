import random
import time

# Truth और Dare की लिस्ट
truths = [
    "🔐 आपके जीवन का वो सबसे बड़ा राज क्या है, जिसे आप कभी किसी से नहीं शेयर कर पाए?",
    "😅 वो सबसे शर्मनाक पल कौन सा था, जिसे याद करके आज भी आप शर्मिंदगी महसूस करते हैं?",
    "🤔 अगर आपको अपनी जिंदगी का सबसे बड़ा डर बताने को कहा जाए, तो वो क्या होगा?",
    "💭 अगर आप एक दिन किसी और के जीवन में जी सकते, तो वो कौन होते और क्यों?",
    "🎯 क्या आपने कभी ऐसा कोई निर्णय लिया है, जिसे आप आज तक नहीं भूल पाए? क्या आप उसे बदलना चाहेंगे?"
]



dares = [
    "💃 अब एक मिनट तक बिना रुके अपने पसंदीदा गाने पर डांस करके दिखाओ जैसे आप डांस किंग/क्वीन हो!",
    "🎤 एक मिनट तक किसी प्रसिद्ध गायक या अभिनेता की आवाज में गाना गाओ और सबको पहचानने दो!",
    "🙃 अब अपनी सबसे अजीब और मजेदार शक्ल बना कर 30 सेकंड तक खड़े रहो, और सबको हंसी में डाल दो!",
    "🎬 अपने पसंदीदा फिल्म सीन को एक्टिंग करते हुए सबको दिखाओ – जितना रोमांटिक हो उतना अच्छा!",
    "🐶 किसी पालतू जानवर की तरह एक्टिंग करो – और 1 मिनट तक उसकी तरह आवाज़ निकालते रहो!"
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
