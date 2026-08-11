# m3

Originally split out of `metabuilder/libraries/` as part of the [reposplit](https://github.com/johndoe6345789/reposplit) effort, then split further into one repo per folder:

- [components](https://github.com/johndoe6345789/components)
- [icons](https://github.com/johndoe6345789/icons)
- [scss](https://github.com/johndoe6345789/scss)
- [hooks](https://github.com/johndoe6345789/hooks)
- [types](https://github.com/johndoe6345789/types)
- [redux](https://github.com/johndoe6345789/redux)
- [interfaces](https://github.com/johndoe6345789/interfaces)
- [schemas](https://github.com/johndoe6345789/schemas)
- [translations](https://github.com/johndoe6345789/translations)

This repo now just holds `checkout.py`, a small script to clone all of them into sibling directories for local dev:

```bash
python3 checkout.py --dest ./workspace
```
