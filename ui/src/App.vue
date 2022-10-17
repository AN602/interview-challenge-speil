<template>
  <v-app>
    <v-main style="width: 800px; margin: 100px auto 0">
      <v-card flat title color="" style="margin-bottom: 1em">
        <br />
        <v-card-title style="text-align: center; font-size: 40px"
          >Breast Cancer Classifier</v-card-title
        >
        <br />
        <v-card-text>
          <br />
          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider1.val"
                :color="slider1.color"
                class="align-center"
                :max="slider1.max"
                :min="slider1.min"
                hide-details
                thumb-label="always"
                :label="slider1.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider1.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider2.val"
                :color="slider2.color"
                class="align-center"
                :max="slider2.max"
                :min="slider2.min"
                hide-details
                thumb-label="always"
                :label="slider2.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider2.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider3.val"
                :color="slider3.color"
                class="align-center"
                :max="slider3.max"
                :min="slider3.min"
                hide-details
                thumb-label="always"
                :label="slider3.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider3.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider4.val"
                :color="slider4.color"
                class="align-center"
                :max="slider4.max"
                :min="slider4.min"
                hide-details
                thumb-label="always"
                :label="slider4.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider4.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider5.val"
                :color="slider5.color"
                class="align-center"
                :max="slider5.max"
                :min="slider5.min"
                hide-details
                thumb-label="always"
                :label="slider5.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider5.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider6.val"
                :color="slider6.color"
                class="align-center"
                :max="slider6.max"
                :min="slider6.min"
                hide-details
                thumb-label="always"
                :label="slider6.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider6.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider7.val"
                :color="slider7.color"
                class="align-center"
                :max="slider7.max"
                :min="slider7.min"
                hide-details
                thumb-label="always"
                :label="slider7.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider7.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider8.val"
                :color="slider8.color"
                class="align-center"
                :max="slider8.max"
                :min="slider8.min"
                hide-details
                thumb-label="always"
                :label="slider8.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider8.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider9.val"
                :color="slider9.color"
                class="align-center"
                :max="slider9.max"
                :min="slider9.min"
                hide-details
                thumb-label="always"
                :label="slider9.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider9.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>

          <v-row>
            <v-col class="pr-4">
              <v-slider
                v-model="slider10.val"
                :color="slider10.color"
                class="align-center"
                :max="slider10.max"
                :min="slider10.min"
                hide-details
                thumb-label="always"
                :label="slider10.label"
              >
                <template v-slot:append>
                  <v-text-field
                    v-model="slider10.val"
                    class="mt-0 pt-0"
                    hide-details
                    single-line
                    type="number"
                    style="width: 90px"
                  ></v-text-field>
                </template>
              </v-slider>
            </v-col>
          </v-row>
          <br />
        </v-card-text>
        <br />
        <div class="text-center">
          <v-btn
            class="ma-2"
            :loading="loading"
            :disabled="loading"
            color="orange"
            @click="loader()"
          >
            Start Classification
          </v-btn>
        </div>
        <br />
      </v-card>

      <v-snackbar
        class="snackbar"
        v-model="snackbar"
        timeout="-1"
        @click="snackbar = false"
      >
        {{ result }}
      </v-snackbar>
    </v-main>
  </v-app>
</template>

<style scoped>
.snackbar:hover {
  cursor: pointer;
}
.v-application {
  background-color: #90a9c6;
}
</style>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";
import { inRange } from "./inRange";

export default defineComponent({
  name: "App",

  components: {},

  data() {
    return {
      slider1: {
        label: "Texture Mean",
        val: 9.71,
        min: 9.71,
        max: 39.28,
        color: "orange darken-3",
      },
      slider2: {
        label: "Area Mean",
        val: 14.5,
        min: 14.5,
        max: 2501.0,
        color: "orange darken-3",
      },
      slider3: {
        label: "Concavity Mean",
        val: 0.0,
        min: 0.0,
        max: 0.43,
        color: "orange darken-3",
      },
      slider4: {
        label: "Area SE",
        val: 6.8,
        min: 6.8,
        max: 542.2,
        color: "orange darken-3",
      },
      slider5: {
        label: "Concavity SE",
        val: 0.0,
        min: 0.0,
        max: 0.4,
        color: "orange darken-3",
      },
      slider6: {
        label: "Fractal Dimension SE",
        val: 0.0,
        min: 0.0,
        max: 0.03,
        color: "orange darken-3",
      },
      slider7: {
        label: "Smoothness Worst",
        val: 0.07,
        min: 0.07,
        max: 0.22,
        color: "orange darken-3",
      },
      slider8: {
        label: "Concavity Worst",
        val: 0.0,
        min: 0.0,
        max: 1.25,
        color: "orange darken-3",
      },
      slider9: {
        label: "Symmetry Worst",
        val: 0.16,
        min: 0.16,
        max: 0.66,
        color: "orange darken-3",
      },
      slider10: {
        label: "Fractal Dimension Worst",
        val: 0.06,
        min: 0.06,
        max: 0.21,
        color: "orange darken-3",
      },
      loading: false,
      result: null,
      snackbar: false,
      resultMap: new Map([
        [0, "THE PATIENT IS MORE LIKELY TO HAVE A BENIGN CANCER"],
        [1, "THE PATIENT IS MORE LIKELY TO HAVE A MALIGNANT CANCER"],
      ]),
    };
  },
  methods: {
    loader() {
      if (!inRange(this.slider1.val, this.slider1.min, this.slider1.max)) {
        this.result = `The value for ${this.slider1.label} must be between ${this.slider1.min} and ${this.slider1.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider2.val, this.slider2.min, this.slider2.max)) {
        this.result = `The value for ${this.slider2.label} must be between ${this.slider2.min} and ${this.slider2.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider3.val, this.slider3.min, this.slider3.max)) {
        this.result = `The value for ${this.slider3.label} must be between ${this.slider3.min} and ${this.slider3.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider4.val, this.slider4.min, this.slider4.max)) {
        this.result = `The value for ${this.slider4.label} must be between ${this.slider4.min} and ${this.slider4.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider5.val, this.slider5.min, this.slider5.max)) {
        this.result = `The value for ${this.slider5.label} must be between ${this.slider5.min} and ${this.slider5.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider6.val, this.slider6.min, this.slider6.max)) {
        this.result = `The value for ${this.slider6.label} must be between ${this.slider6.min} and ${this.slider6.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider7.val, this.slider7.min, this.slider7.max)) {
        this.result = `The value for ${this.slider7.label} must be between ${this.slider7.min} and ${this.slider7.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider8.val, this.slider8.min, this.slider8.max)) {
        this.result = `The value for ${this.slider8.label} must be between ${this.slider8.min} and ${this.slider8.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider9.val, this.slider9.min, this.slider9.max)) {
        this.result = `The value for ${this.slider9.label} must be between ${this.slider9.min} and ${this.slider9.max}`;
        this.snackbar = true;
        return;
      }

      if (!inRange(this.slider10.val, this.slider10.min, this.slider10.max)) {
        this.result = `The value for ${this.slider10.label} must be between ${this.slider10.min} and ${this.slider10.max}`;
        this.snackbar = true;
        return;
      }

      this.loading = true;

      axios
        .post(
          `/api/prediction?texture_mean=${this.slider1.val}&area_mean=${this.slider2.val}&concavity_mean=${this.slider3.val}&area_se=${this.slider4.val}&concavity_se=${this.slider5.val}&fractal_dimension_se=${this.slider6.val}&smoothness_worst=${this.slider7.val}&concavity_worst=${this.slider8.val}&symmetry_worst=${this.slider9.val}&fractal_dimension_worst=${this.slider10.val}`
        )
        .then(
          function (response) {
            this.result = this.resultMap.get(response.data);
            this.snackbar = true;
          }.bind(this)
        )
        .catch((error) => {
          console.log(error);
          this.result = error.response.data;
          this.snackbar = true;
        })
        .finally(() => {
          this.loading = false;
        });
    },
  },
});
</script>
