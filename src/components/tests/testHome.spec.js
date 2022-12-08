import { mount, shallowMount } from "@vue/test-utils";
import app from "src/views/Home.vue";
import { describe, it, expect } from "vitest";

describe("Home.vue", () => {

  it("test home authenticated status", () => {
    const wrapper = mount(app);

    expect(wrapper.vm.authenticated).toBe(false);
    expect(wrapper.vm.mainPageMSG1).toBe('Welcome to InfluCo!');
    expect(wrapper.vm.mainPageMSG2).toBe('The world’s most powerful influencer analysis platform');
    expect(wrapper.find("router-link").isVisible()).toBe(true);
    expect(wrapper.findAll("router-link")).toHaveLength(2);
  });

  it("test page content", () => { 
    const wrapper = mount(app);
    
    expect(wrapper.html()).toContain('InfluCo')
    expect(wrapper.html()).toContain('Browse')
    expect(wrapper.html()).toContain('Start Browse')
    expect(wrapper.html()).toContain('Register')
    expect(wrapper.html()).toContain('login')
  })

  it("test button numbers", () => {
    const wrapper = mount(app);

    expect(wrapper.find("router-link").isVisible()).toBe(true);
    expect(wrapper.findAll("router-link")).toHaveLength(2);
    expect(wrapper.findAll("button")).toHaveLength(1);
  });

  it("test login home page", () => {
    const wrapper = mount(app);

    wrapper.setData({ authenticated: true });
    expect(wrapper.findAll("router-link")).toHaveLength(2);
  });
});