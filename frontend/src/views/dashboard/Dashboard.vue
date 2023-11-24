<script setup lang="ts">
import { ref } from "vue";

import ProductMonthTable from "./dashboardComponents/project-month-table/ProductMonthTable.vue";
</script>

<template>
  
  <v-row>
    <!-- <v-col cols="12" lg="4" class="d-flex align-items-stretch">
      <DailyActivities />
    </v-col> -->
    <v-col cols="12" lg="20" class="d-flex align-items-stretch">
      <ProductMonthTable />
    </v-col>
    <!-- <v-col cols="12" sm="12">
    <BlogCard />
    </v-col> -->
  </v-row>
</template>
