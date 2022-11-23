import { createWebHistory, createRouter } from "vue-router";
import Home from "@/views/Home.vue";
import About from "@/views/AboutView.vue";
import Search from "@/views/SearchView.vue";
import Popular from "@/views/PopularView.vue";
import Dashboard from "@/views/DashboardView.vue";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/search",
    name: "Search",
    component: Search,
  },
  {
    path: "/popular",
    name: "Popular",
    component: Popular,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;