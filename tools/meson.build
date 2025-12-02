generate = find_program('generate.py')
meson.override_find_program('pygi_stubs_generate', generate)

update_all = find_program('update_all.py')
run_target('update-stubs', command: [update_all])
