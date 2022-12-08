import { mount } from "@vue/test-utils";
import search from "src/views/SearchView.vue";
import { describe, it, expect } from "vitest";

describe("SearchView.vue", () => {

  it("test data states", () => {
    const wrapper = mount(search);
    
    expect(wrapper.vm.username).toBe(null);
    expect(wrapper.vm.tag).toBe('');
    expect(wrapper.vm.influencers).toBe(0);
    expect(wrapper.vm.copy_influencers).toBe(0);
    expect(wrapper.vm.origin_influencers).toBe(0);
    expect(wrapper.vm.startIndex).toBe(1);
    expect(wrapper.vm.left).toBe(false);
    expect(wrapper.vm.right).toBe(false);
    expect(wrapper.vm.selected).toBe('');
    expect(wrapper.vm.isLoading).toBe(false);
    expect(wrapper.vm.isShowing).toBe(false);
    expect(wrapper.vm.showAuthorIndex).toBe(0);
    expect(wrapper.vm.startIndexTag).toBe(0);
    expect(wrapper.vm.allTagsLength).toBe(0);
    expect(wrapper.vm.activeBtn).toBe(0);
    expect(wrapper.vm.curPage).toBe(1);
    expect(wrapper.vm.activeTag).toBe('');


  });

  it("test page content", () => { 
    const wrapper = mount(search);
    
    expect(wrapper.html()).toContain('Search')
  })

  it("test button numbers", () => {
    const wrapper = mount(search);

    expect(wrapper.findAll("button")).toHaveLength(1);
  });
});