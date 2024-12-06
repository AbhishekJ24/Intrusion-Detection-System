import js from "@eslint/js";
import pluginReact from "eslint-plugin-react";
import globals from "globals";
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "typescript-eslint";
import eslintPluginPrettierRecommended from "eslint-plugin-prettier/recommended";
import eslintImport from "eslint-plugin-import";

export default tseslint.config(
  pluginReact.configs.flat.recommended,
  pluginReact.configs.flat["jsx-runtime"],
  eslintPluginPrettierRecommended,
  eslintImport.flatConfigs.recommended,
  ...tseslint.configs.recommended,
  {
    ignores: [
      "dist",
      "eslint.config.js",
      "tailwind.config.js",
      "vite.config.ts",
    ],
  },

  {
    extends: [js.configs.recommended, ...tseslint.configs.recommended],
    files: ["**/*.{ts,tsx}"],

    settings: {
      react: {
        version: "detect",
      },

      "import/resolver": {
        typescript: {
          project: [
            "./tsconfig.app.json",
            "./tsconfig.json",
            ".tsconfig.node.json",
          ],
        },
      },
    },

    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        project: ["./tsconfig.node.json", "./tsconfig.app.json"],
        tsconfigRootDir: import.meta.dirname,
      },
    },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
      "eslint-plugin-import": eslintImport,
    },
    rules: {
      "@typescript-eslint/no-non-null-assertion": "off",
      ...reactHooks.configs.recommended.rules,
      "react-refresh/only-export-components": [
        "warn",
        { allowConstantExport: true },
      ],
      "no-console": ["error", { allow: ["warn", "error"] }],
      "arrow-body-style": "off",
      "prefer-arrow-callback": "off",
      "import/no-duplicates": "error",
      "import/prefer-default-export": "off",
      "import/no-default-export": "error",
      "import/named": "error",
    },
  },
);
