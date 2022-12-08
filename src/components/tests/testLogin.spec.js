import { mount } from "@vue/test-utils";
import loginView from "src/views/LoginView.vue";
import { describe, it, expect } from "vitest";

describe("LoginView.vue", () => {

  it("test login states", () => {
    const wrapper = mount(loginView);

    expect(wrapper.vm.username).toBe('');
    expect(wrapper.vm.password).toBe('');
    expect(wrapper.vm.alert).toBe('');
    expect(wrapper.find("router-link").isVisible()).toBe(true);

    expect(wrapper.html()).toContain('Username')
    expect(wrapper.html()).toContain('Password')
    expect(wrapper.html()).toContain('Log in')
    expect(wrapper.html()).toContain('register')
  });

  it("test page content", () => { 
    const wrapper = mount(loginView);
    
    expect(wrapper.html()).toContain('Username')
    expect(wrapper.html()).toContain('Password')
    expect(wrapper.html()).toContain('Log in')
    expect(wrapper.html()).toContain('register')
  })

  it("test button numbers", () => {
    const wrapper = mount(loginView);

    expect(wrapper.findAll("router-link")).toHaveLength(1);
    expect(wrapper.findAll("button")).toHaveLength(1);
  });

  it("test login home page", async () => {
    const wrapper = mount(loginView);

    wrapper.setData({ username: 'user1000', password: 'user1000', passwordVerify: 'user100' });
    await wrapper.find('input[type=text]').setValue('user1000')
    await wrapper.find('input[type=password]').setValue('user1000')
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.vm.alert).toBe('');
  });
});