import { createRouter, createWebHistory } from "vue-router";

const router = createRouter({
  //history: createWebHistory(import.meta.env.BASE_URL),
  history: createWebHistory("/"),
  routes: [
    {
      path: "/",
      redirect: "/dashboard",
      component: () => import("@/layouts/full/FullLayout.vue"),
      children: [
        {
          name: "Dashboard",
          path: "/dashboard",
          component: () =>
            import("@/views/dashboard/Dashboard.vue"),
        },
        {
          name: "Text Overview",
          path: "/dashboard/text-overview",
          component: () =>
            import("@/views/text-overview/TextCards.vue"),
        },
        {
          name: "Financial Overview",
          path: "/dashboard/fin-overview",
          component: () =>
            import("@/views/fin-overview/Charts.vue"),
        }
      ],
    },
  ],
});

export default router;
