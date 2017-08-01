from raider import RaidParticipant
from datetime import datetime

class Raid:
    def __init__(self, pokemon, gym, end):
        self.pokemon = pokemon
        self.gym = gym
        self.end = end
        self.id = None
        self.embed = None
        self.raiders = set()
        self.messages = []

    def add_raider(self, raiderName, partySize=1, startTime=None):
        raider = RaidParticipant(raiderName, int(partySize), startTime)
        if raider in self.raiders:
            self.raiders.remove(raider)
        self.raiders.add(raider)
        self.update_embed_participants()

    def remove_raider(self, raiderName):
        self.raiders.discard(RaidParticipant(raiderName))
        self.update_embed_participants()

    def get_participant_number(self):
        result = 0
        for raider in self.raiders:
            result += raider.party_size
        return result

    def update_embed_participants(self):
        self.embed.set_footer(text='Participants: ' + str(self.get_participant_number()))

    def get_raiders(self):
        result = 'Here are the ' + str(self.get_participant_number()) + ' participants for raid #' + str(self.id) + ':'
        for raider in self.raiders:
            result += '\n\t' + str(raider)
        return result

    def add_message(self, message):
        self.messages.append(message)

    def __hash__(self):
        return hash((self.pokemon, self.gym, self.end.month, self.end.day, self.end.hour))

    def __eq__(self, other):
        return self.pokemon == other.pokemon and self.gym == other.gym and self.end.month == other.end.month and self.end.day == other.end.day and self.end.hour == other.end.hour

class RaidMap:
    def __init__(self):
        self.raids = dict()
        self.hashedRaids = dict()
        self.raidIdSeed = 0

    def generate_raid_id(self):
        self.raidIdSeed += 1
        return self.raidIdSeed

    def create_raid(self, pokemon, gym, end):
        raid = Raid(pokemon, gym, end)
        # Check to see if this raid was already generated from a different channel
        raidHash = hash(raid)
        if raidHash in self.hashedRaids:
            return self.hashedRaids[raidHash]
        return raid

    def store_raid(self, raid):
        self.raids[str(raid.id)] = raid
        self.hashedRaids[hash(raid)] = raid

    def get_raid(self, raidId):
        return self.raids[str(raidId)]

    def clear_raids(self):
        self.raids.clear()
        self.hashedRaids.clear()