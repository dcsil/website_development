import { mount } from "@vue/test-utils";
import register from "src/views/RegisterView.vue";
import { describe, it, expect } from "vitest";

describe("RegisterView.vue", () => {

  it("test register states", () => {
    const wrapper = mount(register);

    expect(wrapper.vm.username).toBe('');
    expect(wrapper.vm.password).toBe('');
    expect(wrapper.vm.passwordVerify).toBe('');
    expect(wrapper.vm.alert).toBe('');
    expect(wrapper.find("router-link").isVisible()).toBe(true);

    expect(wrapper.html()).toContain('Username')
    expect(wrapper.html()).toContain('Password')
    expect(wrapper.html()).toContain('Verify password')
    expect(wrapper.html()).toContain('Submit')
    expect(wrapper.html()).toContain('login')
  });

  it("test page content", () => { 
    const wrapper = mount(register);
    expect(wrapper.html()).toContain('Username')
    expect(wrapper.html()).toContain('Password')
    expect(wrapper.html()).toContain('Verify password')
    expect(wrapper.html()).toContain('Submit')
    expect(wrapper.html()).toContain('login')
  })

  it("test button numbers", () => {
    const wrapper = mount(register);

    expect(wrapper.findAll("router-link")).toHaveLength(1);
    expect(wrapper.findAll("button")).toHaveLength(1);
  });

  it("test login home page", async () => {
    const wrapper = mount(register);

    wrapper.setData({ username: 'user1000', password: 'user1000', passwordVerify: 'user100' });
    await wrapper.find('input[type=text]').setValue('user1000')
    await wrapper.find('input[type=password]').setValue('user1000')
    await wrapper.find('input[type=password]').setValue('user100')
    await wrapper.find('form').trigger('submit.prevent')
    expect(wrapper.vm.alert).toBe('');
  });
});