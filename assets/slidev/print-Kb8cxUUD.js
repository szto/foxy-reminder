import{d as _,_ as u,y as h,b as a,e as t,x as s,H as c,F as f,Z as v,o as n,$ as g,l as x,g as y}from"../modules/vue-Be3bPvwD.js";import{u as b,d as N,_ as k}from"../index-CLcW5-Tr.js";import{c as m}from"../monaco/bundled-types-BlgSCLB_.js";import{N as w}from"./NoteDisplay-C6TCnnuZ.js";import"../modules/shiki-GPPQWDsF.js";import"../modules/file-saver-DY7lxZlc.js";const H={id:"page-root"},L={class:"m-4"},T={class:"mb-10"},V={class:"text-4xl font-bold mt-2"},B={class:"opacity-50"},D={class:"text-lg"},S={class:"font-bold flex gap-2"},C={class:"opacity-50"},F=t("div",{class:"flex-auto"},null,-1),M={key:0,class:"border-main mb-8"},$=_({__name:"print",setup(j){const{slides:d,total:p}=b();u(`
@page {
  size: A4;
  margin-top: 1.5cm;
  margin-bottom: 1cm;
}
* {
  -webkit-print-color-adjust: exact;
}
html,
html body,
html #app,
html #page-root {
  height: auto;
  overflow: auto !important;
}
`),N({title:`Notes - ${m.title}`});const i=h(()=>d.value.map(o=>{var r;return(r=o.meta)==null?void 0:r.slide}).filter(o=>o!==void 0&&o.noteHTML!==""));return(o,r)=>(n(),a("div",H,[t("div",L,[t("div",T,[t("h1",V,s(c(m).title),1),t("div",B,s(new Date().toLocaleString()),1)]),(n(!0),a(f,null,v(i.value,(e,l)=>(n(),a("div",{key:l,class:"flex flex-col gap-4 break-inside-avoid-page"},[t("div",null,[t("h2",D,[t("div",S,[t("div",C,s(e==null?void 0:e.no)+"/"+s(c(p)),1),g(" "+s(e==null?void 0:e.title)+" ",1),F])]),x(w,{"note-html":e.noteHTML,class:"max-w-full"},null,8,["note-html"])]),l<i.value.length-1?(n(),a("hr",M)):y("v-if",!0)]))),128))])]))}}),G=k($,[["__file","/home/runner/work/foxy-reminder/foxy-reminder/slidev/node_modules/@slidev/client/pages/presenter/print.vue"]]);export{G as default};
