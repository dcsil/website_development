import {createApp} from 'vue'
import App from './App.vue'
import router from './router'
import * as Sentry from "@sentry/vue";
import { BrowserTracing } from "@sentry/tracing";

const app = createApp(App);
app.use(router);
// localStorage.setItem('authenticated', 'false')

Sentry.init({
    app,
    dsn: "https://5e87fe88a910404c9ebf991f0f0f9072@o358880.ingest.sentry.io/4504119925145600",
    integrations: [
      new BrowserTracing({
        routingInstrumentation: Sentry.vueRouterInstrumentation(router),
        tracingOrigins: ["localhost", "influco-web.herokuapp.com/", /^\//],
      }),
    ],
    // Set tracesSampleRate to 1.0 to capture 100%
    // of transactions for performance monitoring.
    // We recommend adjusting this value in production
    tracesSampleRate: 1.0,
  });

 app.mount('#app');
