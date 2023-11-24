<script setup lang="ts">
import { defineProps } from 'vue';

const props = defineProps(['dataProp']);


</script>
<template>
  <!-- ----------------------------------------------------------------------------- -->
  <!-- Props -->
  <!-- ----------------------------------------------------------------------------- -->
  <v-card>
    <template v-slot:title> {{ props.dataProp.date }} </template>

    <template v-slot:subtitle> <a :href="props.dataProp.url" target="_blank">{{ props.dataProp.url }}</a> </template>

    <template v-slot:text> {{ props.dataProp.content }} </template></v-card
  >
</template>
