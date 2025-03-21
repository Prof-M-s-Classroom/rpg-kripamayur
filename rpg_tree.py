class StoryNode:
    def __init__(self, event_number, description, left=None, right=None):
        self.event_number = event_number
        self.description = description
        self.left = left
        self.right = right


class GameDecisionTree:
    def __init__(self):
        self.nodes = {}
        self.root = None

    def insert(self, event_number, description, left_event, right_event):
        if event_number not in self.nodes:
            self.nodes[event_number] = StoryNode(event_number, description)

        if left_event != "-1":
            self.nodes[left_event] = self.nodes.get(left_event, StoryNode(left_event, ""))
            self.nodes[event_number].left = self.nodes[left_event]

        if right_event != "-1":
            self.nodes[right_event] = self.nodes.get(right_event, StoryNode(right_event, ""))
            self.nodes[event_number].right = self.nodes[right_event]
        if self.root is None:
            self.root = self.nodes[event_number]

    def play_game(self):
        current_node = self.root

        while current_node:
            print(f"\n{current_node.description}")
            if not current_node.left and not current_node.right:
                print("\nGame Over!")
                break

            choice = input("Enter 1 or 2: ")
            if choice == "1":
                current_node = current_node.left
            elif choice == "2":
                current_node = current_node.right
            else:
                print("Invalid input")


def load_story(filename, game_tree):
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(" | ")
            if len(parts) == 4:
                event_number, description, left_event, right_event = parts
                game_tree.insert(event_number, description, left_event, right_event)

if __name__ == "__main__":
    game_tree = GameDecisionTree()
    load_story("story.txt", game_tree)
    game_tree.play_game()
