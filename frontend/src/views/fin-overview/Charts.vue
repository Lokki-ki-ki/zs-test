<script setup lang="ts">
import { ref, watch, onMounted } from "vue";
import BaseCard from "@/components/BaseCard.vue";
import TheFinOverview from "@/views/fin-overview/TheFinOverview.vue";
import axios from "@/axios-config";

const companies = ref([ "Ford", "Amazon", "Shell", "Apple"])

const fetchCompanyList = async () => {
  try {
    const response = await axios.get("/api/companies"); // Replace with your backend endpoint
    companies.value = response.data.data;
  } catch (error) {
    console.error("Error fetching company list:", error);
  }
};

const company = ref("");

const selectedCompany = ref({});

watch(company, (newValue) => {
  selectedCompany.value = { name: newValue };
});

onMounted(() => {
  fetchCompanyList();
});
</script>

<template>
  <v-row>
    <v-col cols="12" sm="12">
      <BaseCard heading="Anchor">
        <div>
          <p class="text-subtitle-1 text-grey-darken-1">
          Please select the companies you would like to check the financial ratios.
          </p>

          <div class="text-center mt-4">
            <v-select v-model="company" :items="companies" label="Companies"></v-select>
          </div>
        </div>
      </BaseCard>
    </v-col>

    <v-col cols="12" sm="12">
      <TheFinOverview :companySelected="selectedCompany"/>
    </v-col>
  </v-row>
</template>
