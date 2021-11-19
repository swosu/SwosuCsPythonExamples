print('You return to your cabin from a long hunt to find that is has been ravaged. The door has been ripped off and the walls are covered in long cuts. The beast has finally decided to make a move after years. All you have are')
print('What do you do?')
print('(Enter number next to desired action)')
print('1. Enter the forest to set a trap')
print('2. Ask around town for rumors')
ans = int(input('Enter number: \n'))
if ans == 1:
  print('You gather your hunting traps from the disheveled hut, coupled with the meat that you had just collected from your hunt. You leave the clearing, and go past the treeline.')
  print('Upon entering the forest you think of a couple good areas for traps.')
  print('1. Foothold trap placed at a nearby pond')
  print("2. Create a pitfall trap near the game trail")
  ans = int(input('Enter number: \n'))
  if ans == 1:
    print("You know for a fact that the beast frequents this watering hole and have been making sure to not enter this area, until now. After walking for around a while you eventually reach the pond. It's murky water reflects the morning sun. There are spots of mud where animals have covered themselves to cool off. There is also a patch of berry bushes on the eastern coast.")
    print('Where do you place the traps?')
    print('1. Mud rut')
    print('2. Berry bushes')
    ans = int(input('Enter a number: \n'))
    if ans == 1:
      print('You make your way over to the mud ruts and set the trap right in front of the biggest one, which is about 7 feet around. There are some leaves which you lay on top of the mud covered trap to fully mask it. You lay some of the meat you got from your previous hunt atop the trap. Now with the trap set you have two options. Either wait here with your rifle for the beast to show up, or sneak around the area to potentially catch it off guard.')
      print('1. Circle around area')
      print('2. Wait here for the beast')
      ans = int(input('Enter a number: \n'))
      if ans == 1:
        print('You unsling your rifle and set out to begin circling the surrounding area. You make a little more noise than you anticipated. After your third round circling outward from the pond you stop and realize something. All of the birds have stopped making a sound. An eerie sense of dread begins to mount in you as you begin to frantically scan your surroundings. You did not act soon enough however as a large mass of fur and claws descends upon you.')
        print('You have perished.')
    if ans == 2:
      print('You aproach the nearby brush pile and crawl backwards into it, facing the trap. After what feels like ages the sun is now almost set, but you have yet to see anything. You begin to worry as if night hits, you doubt that you will survive the night. Just as this thought creeps into your mind you hear something aproach the ridge-line. A dark mass of fur slowly creeps over the ledge and is lowered to the ground sniffing. It seems to be following your old trail. As it nears your trap placement it stops and stares at the meat.')
      print('What do you do?')
      print('1. Wait')
      print('2. Shoot now')
      ans = int(input('Enter a number: \n'))
      if ans == 1:
        print('The beast looks at the meat for a moment longer and grimaces, its face contorting horribly. It then peers around looking before spotting your rifle and it rushes.')
        print('You have perished.')
      else:
        print('Without hesitation you pull the trigger which immediately results in the creature being thrown backwards and onto the ground')
        print('You are triumphant!')
  else:
    print('You walk to a nearby game trail that has recently become devoid of, well, game. This trail runs by near to your cabin, being only a hundred yards away.Upon inspection you notice some of the same tracks from around your house. You have a shovel from your house and begin to dig. The effort of construction goes on uninterrupted however every now and then you stop to listen to your surroundings. By sundown you have a pit trap constructed. The fruits of this labor would have to go unappreciated for now though, as soon after a loud roar can be heard coming from the house area. The beast was back and it was done hunting.')
    print('What do you do?')
    print('1. Flee the scene')
    print('2. Hold your ground')
    ans = int(input('Enter a number: \n'))
    if ans == 1:
      print('Deciding its best to put some distance from the beast so that it will move across the trail you being to run. Craching through the brush you try to move as fast as possible before it got near you. This was an error. A clawed paw swipes in from the corner of your vision.')
      print('You have perished.')
    if ans == 2:
     print('You decide to stick next to your trap and potentially lure the beast over the hole. After a few minutes of waiting you hear some leaves move about 10 yards away. A low growl breaks the silence of the evening. It is on the same side of the trap that you are.')
     print('1. Stay put')
     print('Attempt to move around the pit')
     ans = int(input())
     if ans == 1:
       print('You stay put and level your rifle. Its hard to see in the darkening treeline, but a dark mass steps into the path. It suddenly dashes at you as you let loose a shot. It still makes contact with you and as you fall backwards both of you fall into the pit.')
       print('Noble sacrifice.')
    if ans == 2:
      print('You begin to step around the pit while attempting to keep an eye trained on the direction of the growls. Your movement provokes an attack as a crashing black mass rushes at you. You let loose your bullet and it hits the creature as you finish your trip to the other side. The beast stumbles towards you and then drops into your pit.')
      print('You are triumphant!')
else:
  print('You begin to walk down the path towards the town.')
  print('This road takes about an hour to reach the town. After around a quater of an hour you feel as if something is off. You realize that you are no longer alone on this walk.')
  print('1. Raise your gun and walk into the center of the road')
  print('2. Attempt to leave the path')
  ans = int(input('Enter a number: \n'))
  if ans == 1:
    print('You level your rifle and slowly spin around and check your environment. The sound of a stick breaking gives away the direction of your hunter. You turn and wait and begin to focus on a now visible outline of the beast.')
    print('1. Take shot')
    print('2. Wait for better shot')
    ans = int(input('Enter a number: \n'))
    if ans == 1:
      print('You take the shot and hear a yelp followed by a sound of crunching leaves. You celebrate for a moment, however you realize this was a poor decision as a figure leaps out of treeline.')
      print('You have perished.')
    if ans == 2:
      print('You decide to wait just a few moments longer for a potentially better shot. This resulted in a headshot as it seemed to lean forward in an attempt to leap at you.')
      print('You are triumphant!')
  else:
    print('You run off to the side of the road. You do not make it far however as it appears you ran right towards the beast.')
    print('You have perished.')