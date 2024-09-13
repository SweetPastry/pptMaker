<!-- 作者：ZhaoZhenHua
链接：https://zhuanlan.zhihu.com/p/633864747
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。 -->

---
theme: Seriph
class: text-center
highlighter: shiki
# background: '/xxx.jpg'
lineNumbers: false
info: |
## Slidev Starter Template
Presentation slides for developers.

Learn more at [Sli.dev](https://sli.dev)
drawings:
persist: false
transition: slide-left  # fade-out
css: unocss
title: xxxxxx
---

<style scoped>
    section {
    text-align: center;    
    }
</style>

# xxxxxx

##

**xxx**



**2023-06**

<div class="pt-12">
<span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover="bg-white bg-opacity-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
</span>
</div>

<div class="abs-br m-6 flex gap-2">
<button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
</button>
<a href="https://github.com/slidevjs/slidev" target="_blank" alt="GitHub"
    class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon-logo-github />
</a>
</div>

---



## 目 录：

<Toc />

## 这是第一页

### 这是小标题

<v-clicks> <!-- 这是一部一部的显示-->

你好啊！

这是行内公式$x^2+\alpha$

这是行间公式
$$
\cos m \varphi+\mathrm{i} \sin m \varphi=\mathrm{e}^{\mathrm{i} m \varphi}, \cos m \varphi-\mathrm{i} \sin m \varphi=\mathrm{e}^{-\mathrm{i} m \varphi}
$$

</v-clicks>

---

## 这是第二页

### 这是小标题

你好啊！

<img 
src="/demo.jpg" class="m-10 h-120 rounded shadow" 
/>

---

layout: end
<div  align="center">   
<img src="/demo.jpg" width = "400"
/>
</div>

---

# *The End*


```




<!-- 在 Slidev 中，public 目录下的文件会被映射到服务器的根路径 /。因此，当您在代码中引用 public/demo.jpg 时，Slidev 实际上会去查找 public/public/demo.jpg，这导致了文件找不到的错误。

解决方案

您需要将图片引用路径从 public/demo.jpg 修改为 /demo.jpg，以正确地引用 public 目录下的图片。 -->