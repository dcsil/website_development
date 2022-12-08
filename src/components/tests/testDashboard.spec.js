import { mount } from "@vue/test-utils";
import dashboard from "src/views/DashboardView.vue";
import { describe, it, expect } from "vitest";

describe("DashboardView.vue", () => {

  it("test data states", () => {
    const wrapper = mount(dashboard);
    
    expect(wrapper.vm.username).toBe(null);
    expect(wrapper.vm.history).toBe(null);
    expect(wrapper.vm.likes).toBe(null);
    expect(wrapper.vm.historyInfluencers).toStrictEqual([]);
    expect(wrapper.vm.likesInfluencers).toStrictEqual([]);
    expect(wrapper.vm.historyActivated).toBe(false);
    expect(wrapper.vm.likesActivated).toBe(false);
    expect(wrapper.vm.resetUsernameActivated).toBe(false);
    expect(wrapper.vm.resetPasswordActivated).toBe(false);

  });

  it("test page content", () => { 
    const wrapper = mount(dashboard);
    
    expect(wrapper.html()).toContain('Account')
    expect(wrapper.html()).toContain('Reset Username')
    expect(wrapper.html()).toContain('Reset Password')
    expect(wrapper.html()).toContain('Logout')
    expect(wrapper.html()).toContain('History')
    expect(wrapper.html()).toContain('Favourit')
    expect(wrapper.html()).toContain('Dashboard')
    expect(wrapper.html()).toContain('Recent Viewed')
    expect(wrapper.html()).toContain('Recent Favourite')
  })

  it("test button numbers", () => {
    const wrapper = mount(dashboard);

    expect(wrapper.findAll("router-link")).toHaveLength(0);
    expect(wrapper.findAll("button")).toHaveLength(2);
  });
});