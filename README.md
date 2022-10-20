# Manifest Schema

This project contains publicly available json schemas that define slacks `manifest.json` application file.

**Guide Outline**:

- [Manifest Schema](#manifest-schema)
  - [Usage](#usage)
  - [Project Structure](#project-structure)
    - [`manifest.schema.json`](#manifestschemajson)
    - [`/schemas`](#schemas)
    - [`/tests`](#tests)
    - [`/scripts`](#scripts)
  - [Resources](#resources)

---

## Usage

JSON schemas can be used for various tasks, the goal of this project is to provide a JSON schema that defines slacks `manifest.json` and provides validation and IntelliSense capabilities to developers editing `manifest.json` files in IDE.

<img src="https://user-images.githubusercontent.com/25348381/195903601-ab1e200a-53b0-470a-9374-bad8b93b35fd.gif" width="60%"/>

To get these capabilities simply include the schema in a JSON file

```json
{
  "$schema": "https://raw.githubusercontent.com/slackapi/manifest-schema/main/manifest.schema.json",
  "_metadata":{
    "major_version": 2
  },
  "settings": { ... }
  ...
}
```

## Project Structure

### [`manifest.schema.json`](manifest.schema.json)

This schema is the **main** schema definition for `manifest.json`, this file allows to map versioned schemas based on the version data the user defines in their manifest definition.

### `/schemas`

This folder contains generated schemas for different versions of the `manifest.json`

### `/tests`

This folder contains `python` test that validate the schema against example `manifest.json` files

### `/scripts`

This folder contains `bash` scripts used by maintainers to execute actions on the project. The github actions of this project also uses the script in this folder to execute its actions.

## Resources

- [JSON schema store](https://www.schemastore.org/json/)
- [VS code JSON info](https://code.visualstudio.com/docs/languages/json)
- [JetBrain JSON info](https://www.jetbrains.com/help/idea/json.html)
- [JSON schema doc](https://json-schema.org/)

Refer to the [maintainers_guide](.github/maintainers_guide.md) in order to contribute to this project
