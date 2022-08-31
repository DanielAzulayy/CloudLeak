const mix = require("laravel-mix");
const sidebarItems = require("./src/sidebar-items.json");
const horizontalMenuItems = require("./src/horizontal-menu-items.json");

require("laravel-mix-nunjucks");
const assetsPath = "src/assets/";

// Files loaded from css url()s will be placed alongside our resources
mix.options({
  fileLoaderDirs: {
    fonts: "assets/fonts",
    images: "assets/images",
  },
  hmrOptions: {
    host: "localhost",
    port: "8080",
  },
});

mix
  // Attention: put all generated css files directly into a subfolder
  // of assets/css. Resource loading might fail otherwise.
  .sass(`${assetsPath}scss/app.scss`, "assets/css/main")
  .sass(`${assetsPath}scss/themes/dark/app-dark.scss`, "assets/css/main")
  .sass(`${assetsPath}scss/pages/error.scss`, "assets/css/pages")
  .sass(`${assetsPath}scss/pages/fontawesome.scss`, "assets/css/pages")
  .sass(`${assetsPath}scss/pages/datatables.scss`, "assets/css/pages")
  .sass(`${assetsPath}scss/pages/simple-datatables.scss`, "assets/css/pages")
  .sass(`${assetsPath}scss/iconly.scss`, "assets/css/shared")
  .js(`${assetsPath}js/app.js`, "assets/js")
  .js(`${assetsPath}js/extensions/ui-chartjs.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/datatables.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/bucket-endpoints.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/scan-results.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/newScan.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/simple-datatables.js`, "assets/js/extensions")
  .js(`${assetsPath}js/extensions/dashboard.js`, "assets/js/extensions")
  .js(`${assetsPath}js/pages/horizontal-layout.js`, "assets/js/pages")
  .copy("src/assets/images", "dist/assets/images")
  .copy(
    "node_modules/bootstrap-icons/bootstrap-icons.svg",
    "dist/assets/images"
  )
  // TinyMCE automatically loads css and other resources from its relative path
  // so we need this hotfix to move them to the right places.
  .copy("node_modules/tinymce/skins", "dist/assets/js/extensions/skins")
  // We place all generated css in /assets/css/xxx
  // This is the relative path to the fileLoaderDirs we specified above
  .setResourceRoot("../../../")
  .setPublicPath("dist");

mix.njk("src/*.html", "dist/", {
  ext: ".html",
  watch: true,
  data: {
    web_title: "CloudLeak",
    sidebarItems,
    horizontalMenuItems,
  },
  block: "content",
  envOptions: {
    watch: true,
    noCache: true,
  },
  manageEnv: (nunjucks) => {
    nunjucks.addFilter("containString", (str, containStr) => {
      if (!str.length) return false;
      return str.indexOf(containStr) >= 0;
    });
    nunjucks.addFilter("startsWith", (str, targetStr) => {
      if (!str.length) return false;
      return str.startsWith(targetStr);
    });
  },
});
