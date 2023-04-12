# %% [markdown]
# # Libraries

# %%
from google.colab import drive
drive.mount('/content/drive')

import numpy as np # 1.22.4
import tensorflow as tf # 2.12.0
import matplotlib.pyplot as plt
import pandas as pd
from tqdm import tqdm
from scipy.ndimage import gaussian_filter

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn

# %%
imagenet_classes = ["tench", "goldfish", "great white shark", "tiger shark", "hammerhead shark", "electric ray", "stingray", "rooster", "hen", "ostrich", "brambling", "goldfinch", "house finch", "junco", "indigo bunting", "American robin", "bulbul", "jay", "magpie", "chickadee", "American dipper", "kite (bird of prey)", "bald eagle", "vulture", "great grey owl", "fire salamander", "smooth newt", "newt", "spotted salamander", "axolotl", "American bullfrog", "tree frog", "tailed frog", "loggerhead sea turtle", "leatherback sea turtle", "mud turtle", "terrapin", "box turtle", "banded gecko", "green iguana", "Carolina anole", "desert grassland whiptail lizard", "agama", "frilled-necked lizard", "alligator lizard", "Gila monster", "European green lizard", "chameleon", "Komodo dragon", "Nile crocodile", "American alligator", "triceratops", "worm snake", "ring-necked snake", "eastern hog-nosed snake", "smooth green snake", "kingsnake", "garter snake", "water snake", "vine snake", "night snake", "boa constrictor", "African rock python", "Indian cobra", "green mamba", "sea snake", "Saharan horned viper", "eastern diamondback rattlesnake", "sidewinder rattlesnake", "trilobite", "harvestman", "scorpion", "yellow garden spider", "barn spider", "European garden spider", "southern black widow", "tarantula", "wolf spider", "tick", "centipede", "black grouse", "ptarmigan", "ruffed grouse", "prairie grouse", "peafowl", "quail", "partridge", "african grey parrot", "macaw", "sulphur-crested cockatoo", "lorikeet", "coucal", "bee eater", "hornbill", "hummingbird", "jacamar", "toucan", "duck", "red-breasted merganser", "goose", "black swan", "tusker", "echidna", "platypus", "wallaby", "koala", "wombat", "jellyfish", "sea anemone", "brain coral", "flatworm", "nematode", "conch", "snail", "slug", "sea slug", "chiton", "chambered nautilus", "Dungeness crab", "rock crab", "fiddler crab", "red king crab", "American lobster", "spiny lobster", "crayfish", "hermit crab", "isopod", "white stork", "black stork", "spoonbill", "flamingo", "little blue heron", "great egret", "bittern bird", "crane bird", "limpkin", "common gallinule", "American coot", "bustard", "ruddy turnstone", "dunlin", "common redshank", "dowitcher", "oystercatcher", "pelican", "king penguin", "albatross", "grey whale", "killer whale", "dugong", "sea lion", "Chihuahua", "Japanese Chin", "Maltese", "Pekingese", "Shih Tzu", "King Charles Spaniel", "Papillon", "toy terrier", "Rhodesian Ridgeback", "Afghan Hound", "Basset Hound", "Beagle", "Bloodhound", "Bluetick Coonhound", "Black and Tan Coonhound", "Treeing Walker Coonhound", "English foxhound", "Redbone Coonhound", "borzoi", "Irish Wolfhound", "Italian Greyhound", "Whippet", "Ibizan Hound", "Norwegian Elkhound", "Otterhound", "Saluki", "Scottish Deerhound", "Weimaraner", "Staffordshire Bull Terrier", "American Staffordshire Terrier", "Bedlington Terrier", "Border Terrier", "Kerry Blue Terrier", "Irish Terrier", "Norfolk Terrier", "Norwich Terrier", "Yorkshire Terrier", "Wire Fox Terrier", "Lakeland Terrier", "Sealyham Terrier", "Airedale Terrier", "Cairn Terrier", "Australian Terrier", "Dandie Dinmont Terrier", "Boston Terrier", "Miniature Schnauzer", "Giant Schnauzer", "Standard Schnauzer", "Scottish Terrier", "Tibetan Terrier", "Australian Silky Terrier", "Soft-coated Wheaten Terrier", "West Highland White Terrier", "Lhasa Apso", "Flat-Coated Retriever", "Curly-coated Retriever", "Golden Retriever", "Labrador Retriever", "Chesapeake Bay Retriever", "German Shorthaired Pointer", "Vizsla", "English Setter", "Irish Setter", "Gordon Setter", "Brittany dog", "Clumber Spaniel", "English Springer Spaniel", "Welsh Springer Spaniel", "Cocker Spaniel", "Sussex Spaniel", "Irish Water Spaniel", "Kuvasz", "Schipperke", "Groenendael dog", "Malinois", "Briard", "Australian Kelpie", "Komondor", "Old English Sheepdog", "Shetland Sheepdog", "collie", "Border Collie", "Bouvier des Flandres dog", "Rottweiler", "German Shepherd Dog", "Dobermann", "Miniature Pinscher", "Greater Swiss Mountain Dog", "Bernese Mountain Dog", "Appenzeller Sennenhund", "Entlebucher Sennenhund", "Boxer", "Bullmastiff", "Tibetan Mastiff", "French Bulldog", "Great Dane", "St. Bernard", "husky", "Alaskan Malamute", "Siberian Husky", "Dalmatian", "Affenpinscher", "Basenji", "pug", "Leonberger", "Newfoundland dog", "Great Pyrenees dog", "Samoyed", "Pomeranian", "Chow Chow", "Keeshond", "brussels griffon", "Pembroke Welsh Corgi", "Cardigan Welsh Corgi", "Toy Poodle", "Miniature Poodle", "Standard Poodle", "Mexican hairless dog (xoloitzcuintli)", "grey wolf", "Alaskan tundra wolf", "red wolf or maned wolf", "coyote", "dingo", "dhole", "African wild dog", "hyena", "red fox", "kit fox", "Arctic fox", "grey fox", "tabby cat", "tiger cat", "Persian cat", "Siamese cat", "Egyptian Mau", "cougar", "lynx", "leopard", "snow leopard", "jaguar", "lion", "tiger", "cheetah", "brown bear", "American black bear", "polar bear", "sloth bear", "mongoose", "meerkat", "tiger beetle", "ladybug", "ground beetle", "longhorn beetle", "leaf beetle", "dung beetle", "rhinoceros beetle", "weevil", "fly", "bee", "ant", "grasshopper", "cricket insect", "stick insect", "cockroach", "praying mantis", "cicada", "leafhopper", "lacewing", "dragonfly", "damselfly", "red admiral butterfly", "ringlet butterfly", "monarch butterfly", "small white butterfly", "sulphur butterfly", "gossamer-winged butterfly", "starfish", "sea urchin", "sea cucumber", "cottontail rabbit", "hare", "Angora rabbit", "hamster", "porcupine", "fox squirrel", "marmot", "beaver", "guinea pig", "common sorrel horse", "zebra", "pig", "wild boar", "warthog", "hippopotamus", "ox", "water buffalo", "bison", "ram (adult male sheep)", "bighorn sheep", "Alpine ibex", "hartebeest", "impala (antelope)", "gazelle", "arabian camel", "llama", "weasel", "mink", "European polecat", "black-footed ferret", "otter", "skunk", "badger", "armadillo", "three-toed sloth", "orangutan", "gorilla", "chimpanzee", "gibbon", "siamang", "guenon", "patas monkey", "baboon", "macaque", "langur", "black-and-white colobus", "proboscis monkey", "marmoset", "white-headed capuchin", "howler monkey", "titi monkey", "Geoffroy's spider monkey", "common squirrel monkey", "ring-tailed lemur", "indri", "Asian elephant", "African bush elephant", "red panda", "giant panda", "snoek fish", "eel", "silver salmon", "rock beauty fish", "clownfish", "sturgeon", "gar fish", "lionfish", "pufferfish", "abacus", "abaya", "academic gown", "accordion", "acoustic guitar", "aircraft carrier", "airliner", "airship", "altar", "ambulance", "amphibious vehicle", "analog clock", "apiary", "apron", "trash can", "assault rifle", "backpack", "bakery", "balance beam", "balloon", "ballpoint pen", "Band-Aid", "banjo", "baluster / handrail", "barbell", "barber chair", "barbershop", "barn", "barometer", "barrel", "wheelbarrow", "baseball", "basketball", "bassinet", "bassoon", "swimming cap", "bath towel", "bathtub", "station wagon", "lighthouse", "beaker", "military hat (bearskin or shako)", "beer bottle", "beer glass", "bell tower", "baby bib", "tandem bicycle", "bikini", "ring binder", "binoculars", "birdhouse", "boathouse", "bobsleigh", "bolo tie", "poke bonnet", "bookcase", "bookstore", "bottle cap", "hunting bow", "bow tie", "brass memorial plaque", "bra", "breakwater", "breastplate", "broom", "bucket", "buckle", "bulletproof vest", "high-speed train", "butcher shop", "taxicab", "cauldron", "candle", "cannon", "canoe", "can opener", "cardigan", "car mirror", "carousel", "tool kit", "cardboard box / carton", "car wheel", "automated teller machine", "cassette", "cassette player", "castle", "catamaran", "CD player", "cello", "mobile phone", "chain", "chain-link fence", "chain mail", "chainsaw", "storage chest", "chiffonier", "bell or wind chime", "china cabinet", "Christmas stocking", "church", "movie theater", "cleaver", "cliff dwelling", "cloak", "clogs", "cocktail shaker", "coffee mug", "coffeemaker", "spiral or coil", "combination lock", "computer keyboard", "candy store", "container ship", "convertible", "corkscrew", "cornet", "cowboy boot", "cowboy hat", "cradle", "construction crane", "crash helmet", "crate", "infant bed", "Crock Pot", "croquet ball", "crutch", "cuirass", "dam", "desk", "desktop computer", "rotary dial telephone", "diaper", "digital clock", "digital watch", "dining table", "dishcloth", "dishwasher", "disc brake", "dock", "dog sled", "dome", "doormat", "drilling rig", "drum", "drumstick", "dumbbell", "Dutch oven", "electric fan", "electric guitar", "electric locomotive", "entertainment center", "envelope", "espresso machine", "face powder", "feather boa", "filing cabinet", "fireboat", "fire truck", "fire screen", "flagpole", "flute", "folding chair", "football helmet", "forklift", "fountain", "fountain pen", "four-poster bed", "freight car", "French horn", "frying pan", "fur coat", "garbage truck", "gas mask or respirator", "gas pump", "goblet", "go-kart", "golf ball", "golf cart", "gondola", "gong", "gown", "grand piano", "greenhouse", "radiator grille", "grocery store", "guillotine", "hair clip", "hair spray", "half-track", "hammer", "hamper", "hair dryer", "hand-held computer", "handkerchief", "hard disk drive", "harmonica", "harp", "combine harvester", "hatchet", "holster", "home theater", "honeycomb", "hook", "hoop skirt", "gymnastic horizontal bar", "horse-drawn vehicle", "hourglass", "iPod", "clothes iron", "carved pumpkin", "jeans", "jeep", "T-shirt", "jigsaw puzzle", "rickshaw", "joystick", "kimono", "knee pad", "knot", "lab coat", "ladle", "lampshade", "laptop computer", "lawn mower", "lens cap", "letter opener", "library", "lifeboat", "lighter", "limousine", "ocean liner", "lipstick", "slip-on shoe", "lotion", "music speaker", "loupe magnifying glass", "sawmill", "magnetic compass", "messenger bag", "mailbox", "tights", "one-piece bathing suit", "manhole cover", "maraca", "marimba", "mask", "matchstick", "maypole", "maze", "measuring cup", "medicine cabinet", "megalith", "microphone", "microwave oven", "military uniform", "milk can", "minibus", "miniskirt", "minivan", "missile", "mitten", "mixing bowl", "mobile home", "ford model t", "modem", "monastery", "monitor", "moped", "mortar and pestle", "graduation cap", "mosque", "mosquito net", "vespa", "mountain bike", "tent", "computer mouse", "mousetrap", "moving van", "muzzle", "metal nail", "neck brace", "necklace", "baby pacifier", "notebook computer", "obelisk", "oboe", "ocarina", "odometer", "oil filter", "pipe organ", "oscilloscope", "overskirt", "bullock cart", "oxygen mask", "product packet / packaging", "paddle", "paddle wheel", "padlock", "paintbrush", "pajamas", "palace", "pan flute", "paper towel", "parachute", "parallel bars", "park bench", "parking meter", "railroad car", "patio", "payphone", "pedestal", "pencil case", "pencil sharpener", "perfume", "Petri dish", "photocopier", "plectrum", "Pickelhaube", "picket fence", "pickup truck", "pier", "piggy bank", "pill bottle", "pillow", "ping-pong ball", "pinwheel", "pirate ship", "drink pitcher", "block plane", "planetarium", "plastic bag", "plate rack", "farm plow", "plunger", "Polaroid camera", "pole", "police van", "poncho", "pool table", "soda bottle", "plant pot", "potter's wheel", "power drill", "prayer rug", "printer", "prison", "missile", "projector", "hockey puck", "punching bag", "purse", "quill", "quilt", "race car", "racket", "radiator", "radio", "radio telescope", "rain barrel", "recreational vehicle", "fishing casting reel", "reflex camera", "refrigerator", "remote control", "restaurant", "revolver", "rifle", "rocking chair", "rotisserie", "eraser", "rugby ball", "ruler measuring stick", "sneaker", "safe", "safety pin", "salt shaker", "sandal", "sarong", "saxophone", "scabbard", "weighing scale", "school bus", "schooner", "scoreboard", "CRT monitor", "screw", "screwdriver", "seat belt", "sewing machine", "shield", "shoe store", "shoji screen / room divider", "shopping basket", "shopping cart", "shovel", "shower cap", "shower curtain", "ski", "balaclava ski mask", "sleeping bag", "slide rule", "sliding door", "slot machine", "snorkel", "snowmobile", "snowplow", "soap dispenser", "soccer ball", "sock", "solar thermal collector", "sombrero", "soup bowl", "keyboard space bar", "space heater", "space shuttle", "spatula", "motorboat", "spider web", "spindle", "sports car", "spotlight", "stage", "steam locomotive", "through arch bridge", "steel drum", "stethoscope", "scarf", "stone wall", "stopwatch", "stove", "strainer", "tram", "stretcher", "couch", "stupa", "submarine", "suit", "sundial", "sunglasses", "sunglasses", "sunscreen", "suspension bridge", "mop", "sweatshirt", "swim trunks / shorts", "swing", "electrical switch", "syringe", "table lamp", "tank", "tape player", "teapot", "teddy bear", "television", "tennis ball", "thatched roof", "front curtain", "thimble", "threshing machine", "throne", "tile roof", "toaster", "tobacco shop", "toilet seat", "torch", "totem pole", "tow truck", "toy store", "tractor", "semi-trailer truck", "tray", "trench coat", "tricycle", "trimaran", "tripod", "triumphal arch", "trolleybus", "trombone", "hot tub", "turnstile", "typewriter keyboard", "umbrella", "unicycle", "upright piano", "vacuum cleaner", "vase", "vaulted or arched ceiling", "velvet fabric", "vending machine", "vestment", "viaduct", "violin", "volleyball", "waffle iron", "wall clock", "wallet", "wardrobe", "military aircraft", "sink", "washing machine", "water bottle", "water jug", "water tower", "whiskey jug", "whistle", "hair wig", "window screen", "window shade", "Windsor tie", "wine bottle", "airplane wing", "wok", "wooden spoon", "wool", "split-rail fence", "shipwreck", "sailboat", "yurt", "website", "comic book", "crossword", "traffic or street sign", "traffic light", "dust jacket", "menu", "plate", "guacamole", "consomme", "hot pot", "trifle", "ice cream", "popsicle", "baguette", "bagel", "pretzel", "cheeseburger", "hot dog", "mashed potatoes", "cabbage", "broccoli", "cauliflower", "zucchini", "spaghetti squash", "acorn squash", "butternut squash", "cucumber", "artichoke", "bell pepper", "cardoon", "mushroom", "Granny Smith apple", "strawberry", "orange", "lemon", "fig", "pineapple", "banana", "jackfruit", "cherimoya (custard apple)", "pomegranate", "hay", "carbonara", "chocolate syrup", "dough", "meatloaf", "pizza", "pot pie", "burrito", "red wine", "espresso", "tea cup", "eggnog", "mountain", "bubble", "cliff", "coral reef", "geyser", "lakeshore", "promontory", "sandbar", "beach", "valley", "volcano", "baseball player", "bridegroom", "scuba diver", "rapeseed", "daisy", "yellow lady's slipper", "corn", "acorn", "rose hip", "horse chestnut seed", "coral fungus", "agaric", "gyromitra", "stinkhorn mushroom", "earth star fungus", "hen of the woods mushroom", "bolete", "corn cob", "toilet paper"]

# %% [markdown]
# # ClickMe Testing Dataset Processing

# %%
src_path = "../datasets/clickme_test.tfrecords"

AUTO = tf.data.AUTOTUNE
BLUR_KERNEL_SIZE = 10
BLUR_SIGMA = 10

_feature_description = {
      "image"       : tf.io.FixedLenFeature([], tf.string, default_value=''),
      "heatmap"     : tf.io.FixedLenFeature([], tf.string, default_value=''),
      "label"       : tf.io.FixedLenFeature([], tf.int64, default_value=0),
}

def set_size(w,h):
  """Set matplot figure size"""
  plt.rcParams["figure.figsize"] = [w,h]

def show(img, p=False, smooth=False, **kwargs):
  """ Display torch/tf tensor """ 
  try:
    img = img.detach().cpu()
  except:
    img = np.array(img)
  
  img = np.array(img, dtype=np.float32)

  # check if channel first
  if img.shape[0] == 1:
    img = img[0]
  elif img.shape[0] == 3:
    img = np.moveaxis(img, 0, -1)

  # check if cmap
  if img.shape[-1] == 1:
    img = img[:,:,0]

  # normalize
  if img.max() > 1 or img.min() < 0:
    img -= img.min(); img/=img.max()

  # check if clip percentile
  if p is not False:
    img = np.clip(img, np.percentile(img, p), np.percentile(img, 100-p))
  
  if smooth and len(img.shape) == 2:
    img = gaussian_filter(img, smooth)

  plt.imshow(img, **kwargs)
  plt.axis('off')
  plt.grid(None)

def _gaussian_kernel(size, sigma):
  x_range = tf.range(-(size-1)//2, (size-1)//2 + 1, 1)
  y_range = tf.range((size-1)//2, -(size-1)//2 - 1, -1)

  xs, ys = tf.meshgrid(x_range, y_range)
  kernel = tf.exp(-(xs**2 + ys**2)/(2*(sigma**2))) / (2*np.pi*(sigma**2))

  kernel = tf.cast(kernel / tf.reduce_sum(kernel), tf.float32)

  return tf.expand_dims(tf.expand_dims(kernel, axis=-1), axis=-1)

GAUSSIAN_KERNEL = tf.cast(_gaussian_kernel(BLUR_KERNEL_SIZE, BLUR_SIGMA), tf.float32)

def _gaussian_blur(heatmap):
    heatmap = tf.nn.conv2d(heatmap[None, :, :, :], GAUSSIAN_KERNEL, [1, 1, 1, 1], 'SAME')
    return heatmap[0]

def _random_crop(image, heatmap):
  seed = tf.random.uniform([2], maxval=10_000, dtype=tf.int32)
  crop_size = tf.random.uniform([], minval=224, maxval=256, dtype=tf.int32)
  
  cropped_image   = tf.image.stateless_random_crop(image, (crop_size, crop_size, 3), seed=seed)
  cropped_heatmap = tf.image.stateless_random_crop(heatmap, (crop_size, crop_size, 1), seed=seed)

  return cropped_image, cropped_heatmap

def parse_prototype(prototype, training=False):
  data    = tf.io.parse_single_example(prototype, _feature_description)

  image   = tf.io.decode_raw(data['image'], tf.float32)
  image   = tf.reshape(image, (256, 256, 3))
  image   = tf.cast(image, tf.float32)
  
  #heatmap = tf.io.decode_jpeg(data['heatmap'])
  heatmap = tf.io.decode_raw(data['heatmap'], tf.float32)
  heatmap = tf.reshape(heatmap, (256, 256, 1))

  image   = tf.image.resize(image, (224, 224), method='bilinear')
  image   = tf.cast(image, tf.float32)

  heatmap = tf.cast(heatmap, tf.float32)
  heatmap = tf.image.resize(heatmap, (64, 64), method="bilinear")
  heatmap = _gaussian_blur(heatmap)
  heatmap = tf.image.resize(heatmap, (224, 224), method="bilinear")
  heatmap = tf.cast(heatmap, tf.float32)

  label   = tf.cast(data['label'], tf.int32)
  label   = tf.one_hot(label, 1_000)

  return image, heatmap, label

def get_dataset(batch_size, training=False):
    # deterministic_order = tf.data.Options()
    # deterministic_order.experimental_deterministic = True

    dataset = tf.data.TFRecordDataset([src_path], num_parallel_reads=AUTO)
    # dataset = dataset.with_options(deterministic_order) 

    dataset = dataset.map(parse_prototype, num_parallel_calls=AUTO)
    
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.prefetch(AUTO)

    return dataset

def get_dataset1000(batch_size):
    deterministic_order = tf.data.Options()
    deterministic_order.experimental_deterministic = True

    dataset = tf.data.TFRecordDataset([src_path], num_parallel_reads=AUTO)
    dataset = dataset.with_options(deterministic_order) 
      
    # dataset = dataset.map(parse_prototype, num_parallel_calls=AUTO)
    
    # Group the dataset by label and take the first element of each group
    test_dataset = dataset.group_by_window(
        key_func = lambda i, h, l: l,
        reduce_func = lambda key, ds: ds.filter(lambda i, h, l: l == key).take(1),
        window_size = 1,
    )
    
    test_dataset = test_dataset.batch(batch_size, drop_remainder=True)
    test_dataset = test_dataset.prefetch(AUTO)

    return test_dataset

# ds_1000 = get_dataset1000(1000)
# cnt = 0
# label_set = set()
# for imgs, hmps, labels in ds_1000: # image, heatmap, label
#     for img, hmp, label in zip(imgs, hmps, labels):
#       print("\rcnt = %s" % (str(cnt)), end=" ")
#       num = label.numpy().item()
#       if not num in label_set:
#         cnt += 1
#         label_set.add(num)

# print(len(label_set))

dataset = get_dataset(1, False)

print(dataset)


# %% [markdown]
# # Helper Functions

# %%
def _bytes_feature(value):
  """Returns a bytes_list from a string / byte."""
  if isinstance(value, type(tf.constant(0))):
    value = value.numpy() # BytesList won't unpack a string from an EagerTensor.
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))

def _float_feature(value):
  """Returns a float_list from a float / double."""
  return tf.train.Feature(float_list=tf.train.FloatList(value=[value]))

def _int64_feature(value):
  """Returns an int64_list from a bool / enum / int / uint."""
  return tf.train.Feature(int64_list=tf.train.Int64List(value=value))

def serialize_example(image, heatmap, label):
  """
  Creates a tf.train.Example message ready to be written to a file.
  """
  # Create a dictionary mapping the feature name to the 
  # tf.train.Example-compatible data type.
  feature = {
      'image': _bytes_feature(image),
      'heatmap': _bytes_feature(heatmap),
      'label': _int64_feature(label)
      
  }

  example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
  return example_proto.SerializeToString()

def write_tfrecords_1000(path):
  writer = tf.io.TFRecordWriter(path)

  cnt = 0
  label_set = set()
  for image, heatmap, label in get_dataset(1, False):
    # print(label.shape)
    
    label = np.argmax(label.numpy(), axis=-1)
    if label.item() in label_set:
      continue
    cnt += 1
    label_set.add(label.item())

    img = image.numpy().tobytes()
    hmp = heatmap.numpy().tobytes()
    label = tf.cast(label, tf.int64).numpy()
    
    example = serialize_example(img, hmp, label)
    writer.write(example)

    print("\rcnt = %s" % (str(cnt)), end=" ")
    if len(label_set) == 1000:
      break

def write_tfrecords(path, size):
  writer = tf.io.TFRecordWriter(path)

  cnt = 0
  label_dict = {}
  label_set = set()
  for image, heatmap, label in get_dataset(1, False):
    # print(label.shape)
    
    label = np.argmax(label.numpy(), axis=-1)
    label_id = label.item()
    if label_id in label_dict and label_dict[label_id] >= size/1000:
      continue
    cnt += 1
    label_dict[label_id] = label_dict.get(label_id, 0) + 1

    img = image.numpy().tobytes()
    hmp = heatmap.numpy().tobytes()
    label = tf.cast(label, tf.int64).numpy()
    
    example = serialize_example(img, hmp, label)
    writer.write(example)

    if label_dict[label_id] >= size/1000:
      label_set.add(label_id)
    print("\rcnt = %s | %s" % (str(cnt), str(size)), end=" ")

  print(set(range(1000)) - label_set)


# %% [markdown]
# # Generate ClickMe Test 1000

# %%
# One image for one class; 1000 classes in total

size = 1000
tgt_path = "../clickme_test_" + str(size) + ".tfrecords"
write_tfrecords(tgt_path, size)

# %% [markdown]
# # View ClickMe Test 1000

# %%
_feature_description = {
    'image': tf.io.FixedLenFeature([], tf.string),
    'heatmap': tf.io.FixedLenFeature([], tf.string),
    'label': tf.io.FixedLenFeature([], tf.int64),
}

def parse_prototype2(prototype, training=False):
  data    = tf.io.parse_single_example(prototype, _feature_description)

  image   = tf.io.decode_raw(data['image'], tf.float32)
  image   = tf.reshape(image, (224, 224, 3))
  image   = tf.cast(image, tf.float32)
  
  heatmap = tf.io.decode_raw(data['heatmap'], tf.float32)
  heatmap = tf.reshape(heatmap, (224, 224, 1))

  label   = tf.cast(data['label'], tf.int32)
  label   = tf.one_hot(label, 1_000)

  return image, heatmap, label

def get_dataset2(batch_size, training=False):
    deterministic_order = tf.data.Options()
    deterministic_order.experimental_deterministic = True

    dataset = tf.data.TFRecordDataset([tgt_path], num_parallel_reads=AUTO)
    dataset = dataset.with_options(deterministic_order) 

    dataset = dataset.map(parse_prototype2, num_parallel_calls=AUTO)
    
    dataset = dataset.batch(batch_size, drop_remainder=True)
    dataset = dataset.prefetch(AUTO)

    return dataset

# %%
dataset = get_dataset2(10, False)
print(dataset)
cnt = 0
for imgs, hmps, labels in dataset: # image, heatmap, label
  for imgs, hmps, label in zip(imgs, hmps, labels):
    print(imgs.dtype, label.dtype, imgs.shape)
    imgs = tf.cast(imgs, tf.float32).numpy()
    imgs -= imgs.min()
    imgs /= imgs.max()
  
    hmps = tf.cast(hmps, tf.float32).numpy()
  
    show(imgs)
    show(hmps, cmap='jet', alpha=0.3)
    print(imagenet_classes[np.argmax(label)])
    plt.title(f"{hmps.shape} H({hmps.mean()} {hmps.std()}), X({imgs.min()} {imgs.max()})")
    plt.axis('off')
    plt.show()
    print('\n\n\n')

    cnt += 1
    if cnt > 10:
      break
  break

# %%
dataset = get_dataset2(1, False)

label_set = set()
for _, _, label in dataset:
  label_set.add(np.argmax(label))

print(len(label_set))


