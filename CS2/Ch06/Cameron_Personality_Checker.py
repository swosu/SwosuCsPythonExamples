def ask_question(question):
  answer = input(question + " ").strip().lower()
  return answer

def analyze_personality(answers):
  # Analyze the responses and determine the personality type
  extraverted = answers.count('e') > answers.count('i')
  sensing = answers.count('s') > answers.count('n')
  thinking = answers.count('t') > answers.count('f')
  judging = answers.count('j') > answers.count('p')

  personality_type = ''
  if extraverted:
      personality_type += 'E'
  else:
      personality_type += 'I'
  if sensing:
      personality_type += 'S'
  else:
      personality_type += 'N'
  if thinking:
      personality_type += 'T'
  else:
      personality_type += 'F'
  if judging:
      personality_type += 'J'
  else:
      personality_type += 'P'

  return personality_type

def print_personality_definition(personality_type):
  definitions = {
      "ISTJ": "The Inspector - Quiet, serious, responsible, and practical. They have an orderly and methodical approach to life.",
      "ISFJ": "The Protector - Quiet, friendly, responsible, and conscientious. They have a strong sense of duty.",
      "INFJ": "The Counselor - Quietly forceful, original, and sensitive. They have an intuitive understanding of people.",
      "INTJ": "The Mastermind - Independent, original, analytical, and determined. They have an exceptional ability to turn theories into solid plans of action.",
      "ISTP": "The Craftsman - Cool onlookers—quiet, reserved, and analytical. They have a detached and unemotional reasoning.",
      "ISFP": "The Composer - Quiet, friendly, sensitive, and kind. They enjoy the present moment and dislike conflicts.",
      "INFP": "The Healer - Quiet, reflective, and idealistic. They are loyal and adaptable, with a keen insight into people.",
      "INTP": "The Architect - Quiet and contained, flexible, and imaginative. They are curious and creative thinkers.",
      "ESTP": "The Dynamo - Flexible and tolerant, they take a pragmatic approach, focusing on immediate results.",
      "ESFP": "The Performer - Outgoing, friendly, and accepting. They are adaptable, action-oriented, and love to make things happen.",
      "ENFP": "The Champion - Enthusiastic, creative, and sociable. They are energetic and warm, and they enjoy exploring possibilities.",
      "ENTP": "The Visionary - Enthusiastic, innovative, and outgoing. They are lively and inventive, and they are often the life of the party.",
      "ESTJ": "The Supervisor - Practical, realistic, and matter-of-fact. They are decisive and quickly move to implement decisions.",
      "ESFJ": "The Provider - Warm-hearted, conscientious, and cooperative. They are dependable and nurturing.",
      "ENFJ": "The Teacher - Warm, empathetic, and responsible. They have excellent people skills and are passionate about helping others.",
      "ENTJ": "The Commander - Frank, decisive, and strong-willed. They are natural leaders, and they quickly take charge of any situation.",
      "ESTJ": "The Supervisor - Practical, realistic, and matter-of-fact. They are decisive and quickly move to implement decisions.",
      "ESFJ": "The Provider - Warm-hearted, conscientious, and cooperative. They are dependable and nurturing.",
      "ENFJ": "The Teacher - Warm, empathetic, and responsible. They have excellent people skills and are passionate about helping others.",
      "ENTJ": "The Commander - Frank, decisive, and strong-willed. They are natural leaders, and they quickly take charge of any situation.",
      "ENTJ": "The Commander - Frank, decisive, and strong-willed. They are natural leaders, and they quickly take charge of any situation.",
      "ESTJ": "The Supervisor - Practical, realistic, and matter-of-fact. They are decisive and quickly move to implement decisions.",
      "ESFJ": "The Provider - Warm-hearted, conscientious, and cooperative. They are dependable and nurturing.",
      "ENFJ": "The Teacher - Warm, empathetic, and responsible. They have excellent people skills and are passionate about helping others.",
      "ENTJ": "The Commander - Frank, decisive, and strong-willed. They are natural leaders, and they quickly take charge of any situation."
      # Add more personality types and their definitions as needed
  }
  print("Your personality type is:", personality_type)
  print("Definition:", definitions.get(personality_type, "Sorry, the definition for this personality type is not available."))

def main():
  print("Answer the following questions with 'yes' or 'no'.")
  print("For each question, type 'e' if your answer is yes and 'i' if your answer is no.")
  print("E.g., if your answer is yes to the first question, type 'e'.")
  questions = [
      "Do you prefer to focus on the outer world (Extraversion) or your own inner world (Introversion)?",
      "Do you prefer to focus on the basic information you take in (Sensing) or interpret and add meaning (Intuition)?",
      "When making decisions, do you prefer to first look at logic and consistency (Thinking) or look at the people and special circumstances (Feeling)?",
      "In dealing with the outside world, do you prefer to get things decided (Judging) or stay open to new information and options (Perceiving)?",
      "Do you prefer to follow a planned and organized approach in your daily life?",
      "Are you more likely to trust your experience rather than seek out new experiences?",
      "Do you find it easy to express your feelings and emotions to others?",
      "Are you more comfortable with routine tasks rather than spontaneous activities?",
      "Do you prefer to spend time alone rather than in large social gatherings?",
      "When faced with a problem, do you prefer to rely on your instincts or analyze the situation logically?",
      "Do you enjoy completing tasks step by step rather than multitasking?",
      "Are you often described as reserved or quiet in social situations?",
      "Do you tend to seek out adventure and excitement?",
      "Do you make decisions based on facts and evidence rather than emotions?",
      "Are you more focused on the present moment rather than future possibilities?",
      "Do you find it easy to adapt to new situations and changes?",
      "Are you more interested in understanding how things work rather than their practical application?",
      "Do you enjoy debates and discussions, even if they may become confrontational?",
      "Do you prefer to have a few close relationships rather than many casual acquaintances?",
      "Are you more inclined to plan your activities in advance rather than being spontaneous?",
      "Do you often find yourself lost in thought, contemplating various ideas and possibilities?",
      "Do you prefer to work independently rather than in a team?",
      "Are you good at managing your time and sticking to schedules?",
      "Do you prefer to have a clear set of rules and guidelines rather than improvising?",
      "Are you more interested in exploring abstract concepts rather than practical applications?",
      "Do you often seek out new experiences and adventures?",
      "Do you enjoy analyzing complex problems and finding creative solutions?",
      "Are you comfortable taking charge and leading a group?",
      "Do you value honesty and straightforwardness in your interactions with others?"
  ]

  answers = []
  for question in questions:
      answer = ask_question(question)
      answers.append(answer)

  personality_type = analyze_personality(answers)
  print_personality_definition(personality_type)

if __name__ == "__main__":
  main()
