
<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import axios from "@/axios-config";

import BaseCard from "@/components/BaseCard.vue";
import CardsSlots from "@/components/vuetifyComponents/cards/CardsSlots.vue";

const fetchCompanyList = async () => {
  try {
    const response = await axios.get("/api/companies"); // Replace with your backend endpoint
    companies.value = response.data.data;
  } catch (error) {
    console.error("Error fetching company list:", error);
  }
};

const fetchCardDataList = async () => {
  try {
    const response = await axios.get(`/reports/companies/${company.value}`);
    cardDataList.value = response.data.data;
  } catch (error) {
    console.error("Error fetching card data list:", error);
  }
};

const cardDataList = ref([])

const companies = ref(["Company 1", "Company 2", "Company 3"]);

const company = ref("Company 1");

const filterCardsByCompany = () => {
  fetchCardDataList();
};
watch(company, filterCardsByCompany);


// Fetch initial data
onMounted(() => {
  fetchCompanyList();
  fetchCardDataList(); 
});

</script>


<template>
  <v-row>
  <v-select v-model="company" :items="companies" label="Company" item-text="name" item-value="id"></v-select>

  <v-col v-for="(cardData, index) in cardDataList" :key="index" cols="12" sm="12" lg="12">
    <BaseCard :heading="cardData.heading">
      <CardsSlots :dataProp="cardData"/>
    </BaseCard>
  </v-col>
  </v-row>
</template>
