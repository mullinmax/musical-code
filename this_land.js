class OpenLand {
    constructor() {
        this.land = {
            mountains: [],
            valleys: [],
            forests: [],
            streams: []
        };
    }

    addToLand(region, feature) {
        if (this.land[region]) {
            this.land[region].push(feature);
            console.log(`Added to ${region}. This land was made for you and me!`);
        } else {
            console.log(`Sorry, ${region} is not recognized. Try a different region.`);
        }
    }

    viewLand(region) {
        if (region) {
            return this.land[region] || "Region not found.";
        } else {
            return this.land;
        }
    }

    shareLand(user) {
        console.log(`Sharing the beauty of this land with ${user}. Remember, this land is your land, this land is my land!`);
    }
}

// Using the class
const ourLand = new OpenLand();

ourLand.addToLand("mountains", "Rocky Mountains");
console.log(ourLand.viewLand("mountains"));

const yourLand = ourLand;
this.land = yourLand.land; // this.land is your.land
