from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ✅ Realistic classification for many common waste items
classification_rules = {
    "plastic bottle": {
        "category": "Recyclable - Plastic",
        "tip": "Rinse and place it in your recycling bin.",
        "reuse_idea": "Make planters, bird feeders, or DIY crafts."
    },
    "banana peel": {
        "category": "Organic Waste",
        "tip": "Best composted at home or through local composting.",
        "reuse_idea": "Use in compost, garden fertilizer, or shoe polish."
    },
    "paper": {
        "category": "Recyclable - Paper",
        "tip": "Keep it dry and place in your paper recycling bin.",
        "reuse_idea": "Use for notes, gift wrap, or cleaning glass."
    },
    "envelope": {
        "category": "Recyclable - Paper",
        "tip": "Recycle with paper; remove any plastic windows.",
        "reuse_idea": "Turn into bookmarks, scrap paper, or seed holders."
    },
    "newspaper": {
        "category": "Recyclable - Paper",
        "tip": "Recycle or compost if soiled.",
        "reuse_idea": "Wrap gifts or clean windows."
    },
    "cardboard box": {
        "category": "Recyclable - Cardboard",
        "tip": "Flatten boxes and remove tape before recycling.",
        "reuse_idea": "Use for storage, crafts, or moving."
    },
    "can": {
        "category": "Recyclable - Metal",
        "tip": "Rinse before placing in recycling.",
        "reuse_idea": "Use as pen holders, planters, or candle molds."
    },
    "glass bottle": {
        "category": "Recyclable - Glass",
        "tip": "Rinse and recycle if your city accepts glass.",
        "reuse_idea": "Use as vases or storage containers."
    },
    "battery": {
        "category": "Hazardous Waste",
        "tip": "Drop off at e-waste stations or electronics stores.",
        "reuse_idea": "Rechargeable batteries can be reused multiple times."
    },
    "old phone": {
        "category": "Electronic Waste",
        "tip": "Take to an e-waste collection center.",
        "reuse_idea": "Use as security cam or music player."
    },
    "medicine": {
        "category": "Medical Waste",
        "tip": "Return via take-back programs or drugstores.",
        "reuse_idea": "Do not reuse. Dispose safely."
    },
    "clothes": {
        "category": "Textile Waste",
        "tip": "Donate if usable; recycle or repurpose if torn.",
        "reuse_idea": "Make rags, bags, or pet bedding."
    },
    "food waste": {
        "category": "Organic Waste",
        "tip": "Compost if possible; never send to landfill.",
        "reuse_idea": "Make compost or natural fertilizer."
    },
    "plastic bag": {
        "category": "Non-Recyclable - Soft Plastic",
        "tip": "Drop off at store collection points.",
        "reuse_idea": "Reuse as liners, packaging, or crafts."
    }
}

@app.route("/classify", methods=["POST"])
def classify_waste():
    item_name = request.form.get("itemName", "").strip().lower()
    image = request.files.get("image")

    default_response = {
        "category": "Unknown",
        "tip": "Try another name or image. Not found in database.",
        "reuse_idea": "Think creatively — can it be upcycled or donated?"
    }

    result = classification_rules.get(item_name, default_response)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
