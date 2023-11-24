<script setup lang="ts">
import { ref, onMounted, defineProps, watch } from "vue";
import { FinOverviewData } from "./FinOverviewData";
import axios from "@/axios-config";


const elementVisible = ref(false);
const props = defineProps(["companySelected"]);

const fetchData = async () => {
  try {
    // Fetch data from the backend API
    console.log("Fetch Data")
    const response = await axios.get(`/api/fin/${props.companySelected.name}`); // Replace with your backend API endpoint
    FinOverviewData.chartOptions.series = response.data.series;
    FinOverviewData.chartOptions.xaxis = response.data.xaxis;
    elementVisible.value = true;
  } catch (error) {
    console.error("Error fetching sales data:", error);
  }
};

watch(() => props.companySelected, fetchData);
onMounted(fetchData);



</script>


<template>
  <!-- ------------------------------------ -->
  <!-- html -->
  <!-- ------------------------------------ -->
  <v-card>
    <v-card-text class="pa-7">
      <div class="d-sm-flex align-center mb-5">
        <div>
          <h3 class="text-h6 title font-weight-medium">{{ props.companySelected.name}}</h3>
        </div>
        <v-spacer></v-spacer>
      </div>
      <div v-show="elementVisible">
        <apexchart
          type="line"
          height="280px"
          :options="FinOverviewData.chartOptions"
          :series="FinOverviewData.chartOptions.series"
        ></apexchart>
      </div>
    </v-card-text>
  </v-card>
</template>


