<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "@/axios-config";


const select = ref("This Month");
const items = ref(["This Month", "Last Month", "Before Last Month"]);

const monthtable = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get(`/get_data/${select.value}`);
    monthtable.value = response.data.data;
    console.log(response.data);
  } catch (error) {
    console.error("Error fetching data:", error);
  }
});
</script>

<template>
  <v-card flat class="w-100 h-100">
    <v-card-text>
      <div class="d-sm-flex align-center">
        <div>
          <h2 class="title text-h6 font-weight-medium">Reports Overview</h2>
        </div>
        <v-spacer></v-spacer>
        <div class="ml-auto">
          <v-select
            v-model="select"
            :items="items"
            variant="outlined"
            dense
            hide-details
          ></v-select>
        </div>
      </div>
      <v-table class="month-table mt-7">
        <template v-slot:default>
          <thead>
            <tr>
              <th class="font-weight-medium text-subtitle-1">Id</th>
              <th class="font-weight-medium text-subtitle-1">Company Name</th>
              <th class="font-weight-medium text-subtitle-1">Ticker</th>
              <th class="font-weight-medium text-subtitle-1">Number of Reports</th>
              <th class="font-weight-medium text-subtitle-1">Latest Updated</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in monthtable"
              :key="item.id"
              :class="item.activestate"
              class="month-item"
            >
              <td>{{ item.id }}</td>
              <td>
                <h4 class="font-weight-bold text-no-wrap">
                  {{ item.name }}
                </h4>
                <h6
                  class="
                    text-no-wrap
                    font-weight-regular
                    text-body-2 text-grey-darken-1
                  "
                >
                  {{ item.naics }}
                </h6>
              </td>
              <td>
                <v-chip
                  class="ma-2"
                  :color="item.statuscolor"
                  size="small"
                  label
                  >{{ item.ticker }}</v-chip
                >
              </td>
              <td>
                <h4>
                  {{ item.numbers }}
                </h4>
              </td>
              <td>
                <h4>{{ item.date }}</h4>
              </td>
            </tr>
          </tbody>
        </template>
      </v-table>
    </v-card-text>
  </v-card>
</template>
