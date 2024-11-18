def prompt (cat):
  prompt = f"""

I will provide you with an image and the name of the product the girl in the image is wearing. Your task is to answer several questions based on the image and the specified product category.
Based on first Question if a product category  and Sub category is not related to the other question, write "null" as the answer
focus only this type of product in image : {cat} 

1 : Please identify the product sub-category:
Options:

ALL CATEGORIES :
-Dresses:
  A-Line-Dress: a dress fitted at the hips and gradually widens towards the hem, giving the impression of the shape of a capital letter A.
  Sheath-Dress: a form-fitting dress with a defined waist. Its simple, sleek lines skim the body, from the shoulders down to the hips.
  Maxi-Dress: a floor or ankle-length informal dress usually fitted on the top part and loose flowing at the bottom.
  Shift-Dress: a short, sleeveless dress that hangs from the shoulders. It is designed to move with the body and is often adorned with geometric designs.
  Wrap-Dress: a dress with a front closure produced by looping one side over the other and knotting the connecting waist ties or fastening buttons.
  Bodycon-Dress: a tight-fitting dress that is often made from stretchy material. Bodycon (short for body-conscious) dresses are a 'figure hugging' dress style, which is designed to hug every curve.
  Slip-Dress: a sort of clothing that is similar to an underslip or petticoat. It's usually cut on the bias and has spaghetti straps.
  Sun-Dress: a summer dress. It is typically informal or casual clothing in a lightweight fabric with a loose fit.
  Halter-Dress: a dress featuring a halterneck, a style of strap that is tied behind the neck rather than over the shoulders.
  Sweater-Dresses: Dresses made from sweater-like material.
  Midi-Dress: Dresses with a hemline between the knee and ankle.
  Mini-dress: Short dresses above the knee.

-Jumpsuits:
  Boiler-Suits: Loose-fitting, one-piece garments with a front zip.
  Cat-suit: Tight-fitting, one-piece garment covering the torso and legs.
  Denim-Jumpsuits: One-piece garments made from denim.
  Flared-&-Wide-Leg: Jumpsuits with wider leg openings.
  Overalls: Jumpsuits with a bib and shoulder straps.

-Rompers:
  Rompers: Short, one-piece garments covering the torso and shorts.
  Shortall: A type of romper with overall-style straps.


-Top : 
  Blouses: a loose-fitting upper garment, typically worn by women for formal or semi-formal occasions.
  Tank-Top: a sleeveless upper garment with a low neckline.
  Crop-Top: a top that exposes the waist or abdomen.
  Bodysuit: a one-piece form-fitting garment that covers the torso and the crotch.
  Halter-Top: a type of sleeveless top secured around the neck and leaves the back bare.
  Sweater: a knitted garment typically , worn over the upper body.
  Tube-Top: a strapless top held up by elastic.
  T-Shirts: casual upper-body clothes made from cotton or synthetic materials
  Tunics: loose, often long tops that reach at least to the hips and are worn with pants or leggings.
  Button Down: Tops with a full-length button closure.


-Outerwear
  Coats: a long garment worn to keep warm in cold weather. Common types include trench coats, peacoats, and overcoats.
  Jackets: similar to a coat but generally shorter, ending at or around the waist. There are many styles of jackets, including denim jackets, leather jackets, and blazers.
  Ponchos: oversized, loose garments that are worn over the shoulders, often featuring a hole for the head.
  Cardigan: a type of knitted garment that has an open front.
  Vest: a sleeveless garment that covers the upper body.
  Windbreaker: a lightweight jacket designed to resist wind chill and light rain.
  Pea Coat: a heavy wool coat typically featuring a double-breasted front.
  Cape: a sleeveless outer garment that is draped over the shoulders.
  Parka : a type of coat filled with down or synthetic fiber and typically has a fur-lined hood.


-Pant:
  Jeans: a type of pants made from denim. They come in a variety of cuts, including  bootcut, and straight-leg.
  Skinny: Tight-fitting pants.
  Leggings: a type of skin-tight trousers typically made from a blend of lycra, nylon, cotton, or polyester.
  Culottes: knee-length trousers cut with full legs to resemble a skirt.
  Capris: a style of pants that are longer than shorts but are not as long as trousers.
  Jeggings: a type of leggings that are designed to resemble tight denim jeans.
  Harem Pants: baggy, long pants caught in at the ankle.
  Palazzo Pants: long women's trousers cut with a loose, wide leg.
  Shorts: a type of lower-body clothing that covers from the waist to the thighs or just below. They can be casual, like denim shorts, or formal, like tailored shorts.
  Denim-Shorts: Shorts made from denim fabric.

  
-Skirts:
  Maxi-Skirts: Long skirts reaching the ankle.
  Midi-Skirts: Skirts with a hemline between the knee and ankle.
  Mini-Skirts: Short skirts above the knee.
  Pencil-Skirts: Fitted skirts with a straight, narrow cut.
  Wrap-Skirts: Skirts that wrap around and tie at the waist.
  Denim-Skirts: Skirts made from denim fabric.

-Postpartum
  Postpartum: Clothing designed for the period after childbirth.

-Sleep-&-Loungewear
  Sleepwear: Clothing designed for sleeping, including pajamas.
  Loungewear: Comfortable clothing for relaxing at home.

2 : If the product is non-multicolor What is the primary colors of the product?
All color tag : 
Metallic
Neutral
Red
Blue
Green
Yellow
Black
White
Pink
Purple
Orange
Brown
Grey
Multicolor
Beige
Navy
Teal
Maroon
Lavender
Gold
Silver
Rose Gold

	
3 : If the product is multicolor, specify the color combinations (e.g., [color1, color2, etc.]). If the product is not multicolor, select 'None'. Ensure the colors you list are very clear, easily visible, and prominently used in the product

All colors tag :
Metallic
Neutral
Red
Blue
Green
Yellow
Black
White
Pink
Purple
Orange
Brown
Grey
Multicolor
Beige
Navy
Teal
Maroon
Lavender
Gold
Silver
Rose Gold


4 : Is the product color style is  dark or light?
option : 
Dark 
light

5 : What is the main material or fabric of the product?

All material tag : 
Cotton
Polyester
Denim
Wool
Linen
Leather
Nylon
Rayon
Spandex
Acrylic
Blended
Fleece
Velvet
Chiffon
Jersey
Terry Cloth
Tweed
Corduroy
Crochet
Crystal & Gemstones
Cut Out
Eyelet
Faux Fur
Pearl
Ruched
Silk/Satin


6 : Does the product have  patterns?

All patern tag : 
- Abstract
- Animal Print
- Camo
- Floral
- Fruit
- Graphic
- Hearts
- Paisley
- Patterned
- Plaid
- Polka Dot
- Solid Colored
- Stars
- Striped
- Tie Dye
- Ombre
- Tortoise
- Tropical







7 : What types of neckline does the product have?

All neckline style tag : 
Crew-Neck: A rounded, close-fitting neckline that sits at the base of the neck, typically found in t-shirts and sweaters.
V-Neck: A neckline that dips down in the front to form a "V" shape, which can vary in depth.
Scoop-Neck: A wide, rounded neckline that dips lower than a crew neck, often creating a more open and feminine look.
Square-Neck: A neckline that has a straight horizontal line across the front, creating a square shape at the shoulders.
Boat-Neck: A wide, shallow neckline that runs horizontally from shoulder to shoulder, also known as a bateau neckline.
Halter: A neckline that wraps around the back of the neck, leaving the shoulders and back exposed.
Off-Shoulder: A neckline that sits below the shoulders, exposing the collarbone and shoulders, often supported by elastic or straps.
Collared: A neckline with an attached collar, often seen in shirts, blouses, and dresses with button-down fronts.
Turtle-Neck: A high, close-fitting neckline that covers the neck, typically folded over, often seen in sweaters and tops.
Cowl-Neck: A draped, rounded neckline that creates soft folds of fabric.
Sweetheart-Neck: A neckline that is shaped like the top half of a heart, often emphasizing the bust.
Keyhole-Neck: A neckline with a small, round or teardrop-shaped cutout near the collarbone.
High-Neck: A neckline that extends higher up on the neck but isn’t as fitted or folded as a turtleneck.
Plunge-Neck: A deep V-neckline that plunges down the chest, often to a dramatic extent.
One-Shoulder: A neckline that goes across the body from one shoulder, leaving the other shoulder exposed.
Surplice: A neckline created by wrapping or crossing fabric over itself, forming a V-shape.


8 : What types of sleeves does the product have?

All sleeve tags :
Sleeveless: Garments without any sleeves, leaving the shoulders and arms exposed.
Short-Sleeve: Sleeves that cover the shoulders and upper arms, typically ending above the elbow.
Cap-Sleeve: Short sleeves that just cover the shoulder area, often forming a slight cap shape.
3/4-Sleeve : Sleeves that extend to about three-quarters of the way down the arm, typically ending between the elbow and wrist.
Long-Sleeve: Sleeves that fully cover the arms, extending to the wrist.
Puff-Sleeve: Sleeves that are voluminous and gathered at the shoulder or cuff, creating a puffed appearance.






9 : Does the product have  Shoulder styles?

All shoulder style tag:
Regular-Shoulder: The seam sits at the natural shoulder line, providing a classic fit.
Dropped-Shoulder: The seam falls below the natural shoulder line, creating a relaxed and oversized look.
Cold-Shoulder: The shoulder area is cut out, leaving the shoulders exposed while the rest of the sleeve remains intact.
One-Shoulder: The garment has a single strap or sleeve, leaving one shoulder exposed.
Off-Shoulder: The neckline sits below the shoulders, exposing the collarbone and shoulders.
Halter-Shoulder: Straps that wrap around the back of the neck, leaving the shoulders and upper back exposed.
Spaghetti-Shoulder: Very thin straps that leave the shoulders mostly exposed, often seen in camisoles and sundresses.
Puff-Shoulder: Extra fabric or padding at the shoulders creates a puffed, voluminous look.


10 : Does the product have  strap styles?

All  strap style tag:   
Spaghetti-Straps: Thin, delicate straps that resemble spaghetti noodles
Wide-Strap: Straps that are wider, providing more coverage and support.
Halter-Strap: Straps that wrap around the back of the neck, leaving the shoulders and back exposed,
One-Shoulder-Strap: A single strap that goes over one shoulder, leaving the other shoulder exposed, creating an asymmetrical look, 
Shoulder-Ties: Straps that are tied at the shoulders, allowing for adjustable length and a decorative bow or knot
Strapless: Garments that do not have any shoulder straps, relying on the fit around the bust to stay in place


11 : Does the product have  special features or embellishments?

All special features or embellishments:
Pockets: Functional pouches typically sewn into the garment for carrying small items.
Ruffles: Frilly or pleated strips of fabric used for decorative edging or accents.
Lace: Delicate fabric with an open weave pattern, often used for decorative trim or panels.
Embroidery: Decorative stitching or patterns sewn into the fabric, often with thread or yarn.
Beads: Small, decorative spheres or shapes often sewn onto fabric for embellishment.
Sequins: Small, shiny discs sewn onto fabric to create a sparkly effect.
Pleats: Folds of fabric sewn in place to create a structured or textured effect.
Buttons: Small discs used for fastening or decorative purposes, typically with a thread shank.
Zipper: Fastening devices consisting of two strips of teeth that are pulled together by a slider.
Belt: Strip of fabric or leather used to cinch the waist or as a decorative accessory.
Cutouts: Sections of fabric removed to reveal skin or create design elements.
Fringe: Strands of fabric or threads attached to the edge of a garment for a decorative effect.
Tassels: Hanging ornaments made of threads or cords, often decorative and attached to edges.
Ribbons: Strips of fabric used for tying or as decorative elements on garments.
Bow: Fabric loops tied into decorative knots, often used as accents or closures.
Drawstrings: Cords or strings used to adjust the fit or gather fabric
Hood: Attached fabric covering the head and neck
Elasticized Waist: Waistbands made with elastic for comfort and flexibility
Hook: A type of closure consisting of a small hook that catches over a bar or into a loop.
Snap: Small fasteners that make a snapping sound when closed, often metal or plastic.
Ties: Strings or straps that are tied to fasten the garment.
Buckle: A fastener that includes a frame and prong, used to secure belts and straps.


Please provide answers only from the tag listed. If no answer is applicable, respond with "null". Ensure that all answers are in JSON format.
example response : 
{{"product-category":[], sub-category":[], "color":[],"color style":[], "multicolor":[], "material": [],"pattern": [],"sleeve style": [],"shoulder_style":[],"strap_style" : [],"neck_style":[] ,"special features or embellishments": []}}


"""
  return prompt