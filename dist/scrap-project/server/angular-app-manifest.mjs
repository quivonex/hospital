
export default {
  bootstrap: () => import('./main.server.mjs').then(m => m.default),
  inlineCriticalCss: true,
  baseHref: '/',
  locale: undefined,
  routes: [
  {
    "renderMode": 2,
    "redirectTo": "/login",
    "route": "/"
  },
  {
    "renderMode": 2,
    "route": "/home"
  },
  {
    "renderMode": 2,
    "route": "/login"
  },
  {
    "renderMode": 2,
    "route": "/enquiry-form"
  },
  {
    "renderMode": 2,
    "route": "/contact"
  },
  {
    "renderMode": 2,
    "route": "/approve-req"
  },
  {
    "renderMode": 2,
    "route": "/rejected-req"
  },
  {
    "renderMode": 2,
    "route": "/orders"
  },
  {
    "renderMode": 2,
    "route": "/products"
  },
  {
    "renderMode": 2,
    "route": "/sub-products"
  },
  {
    "renderMode": 2,
    "route": "/admin-create"
  },
  {
    "renderMode": 2,
    "route": "/upload-img"
  },
  {
    "renderMode": 2,
    "route": "/complaints"
  }
],
  entryPointToBrowserMapping: undefined,
  assets: {
    'index.csr.html': {size: 1578, hash: 'ec85cc82d4a3a6763227633f73eaa6525546b32e6dc14a144af92fc87d4f3a3c', text: () => import('./assets-chunks/index_csr_html.mjs').then(m => m.default)},
    'index.server.html': {size: 1009, hash: 'beaaff3a31baed28c60e8d23861b96e402771cb08edf7094e47414c049c6baf0', text: () => import('./assets-chunks/index_server_html.mjs').then(m => m.default)},
    'home/index.html': {size: 3633, hash: '5160b90a3271b00671c9ba528448b7fba9cc1a995d978ce624762add7207d784', text: () => import('./assets-chunks/home_index_html.mjs').then(m => m.default)},
    'login/index.html': {size: 7048, hash: 'fdcd4dfba673bdb3ca6e1a3242e791825d05001ca1f694451132be16f50ef12f', text: () => import('./assets-chunks/login_index_html.mjs').then(m => m.default)},
    'contact/index.html': {size: 11186, hash: '27d58b2581ac891412378ee44c3a4a49ea2050bb12e0ecc35acc48e9261f4a3d', text: () => import('./assets-chunks/contact_index_html.mjs').then(m => m.default)},
    'enquiry-form/index.html': {size: 13477, hash: '29d9cb149860b0ec6094abb37031d644a663b7dc660325a9067cacc05d99663a', text: () => import('./assets-chunks/enquiry-form_index_html.mjs').then(m => m.default)},
    'rejected-req/index.html': {size: 12930, hash: '4e0adc0c5f10f0950f6620c14f23b5dc902fff2c764157e76f281b8926ee056e', text: () => import('./assets-chunks/rejected-req_index_html.mjs').then(m => m.default)},
    'products/index.html': {size: 8191, hash: '60e3fdf4be6831afcfb80db7678108689029f6a4c2993b11d55e70dc04e92368', text: () => import('./assets-chunks/products_index_html.mjs').then(m => m.default)},
    'approve-req/index.html': {size: 20191, hash: '97e0e14e925e9d0da47bdf87206b24e9e01e90c830bb3df459d3f8815775047b', text: () => import('./assets-chunks/approve-req_index_html.mjs').then(m => m.default)},
    'sub-products/index.html': {size: 32220, hash: 'a65eaabb30d927c2fa06a45782ae67e58d95c85a8659ad8b648b24f2ecfcd758', text: () => import('./assets-chunks/sub-products_index_html.mjs').then(m => m.default)},
    'orders/index.html': {size: 25034, hash: 'fb1fa7747c89d0669520e544db5deaba1cf43ef3fe2bfc6baab7b7783cd354e6', text: () => import('./assets-chunks/orders_index_html.mjs').then(m => m.default)},
    'upload-img/index.html': {size: 4499, hash: '2f29ca894f05a5cb020f2b201e6246af4b480dd3545c57f696024371a4198011', text: () => import('./assets-chunks/upload-img_index_html.mjs').then(m => m.default)},
    'admin-create/index.html': {size: 6527, hash: 'fc5ff4207b7375ae50da0038d2af6ad24de39c31fef0e825c25ce0f3342c48fc', text: () => import('./assets-chunks/admin-create_index_html.mjs').then(m => m.default)},
    'complaints/index.html': {size: 7172, hash: '2cc7f250fb2047438170d305008aaf085cd56092d16c1bef4316302ac0abf1fd', text: () => import('./assets-chunks/complaints_index_html.mjs').then(m => m.default)},
    'styles-JGX4B2HB.css': {size: 73701, hash: 'Gx2aouZVGDY', text: () => import('./assets-chunks/styles-JGX4B2HB_css.mjs').then(m => m.default)}
  },
};
