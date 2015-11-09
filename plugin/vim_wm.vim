if has('python')
	python import sys
	let s:vim_wm_pyfilepath = expand('<sfile>:r') . '.py'
	function! Vim_Py()
		execute 'pyfile ' s:vim_wm_pyfilepath
	endfunction
	function! Vim_Pos()
		python sys.argv = ["smart"]
		call Vim_Py()
	endfunction
	function! Vim_Size(mode)
		if a:mode == 0
			python sys.argv = ["big"]
		elseif a:mode == 1
			python sys.argv = ["large"]
		elseif a:mode == 2
			python sys.argv = ["default"]
		endif
		call Vim_Py()
	endfunction
	function! Vim_Size_Select()
		if !exists("s:vim_size_select")
			let s:vim_size_select = 0
		endif
		if s:vim_size_select == 0
			call Vim_Size(0)
			let s:vim_size_select = 1
		elseif s:vim_size_select == 1
			call Vim_Size(1)
			let s:vim_size_select = 2
		elseif s:vim_size_select == 2
			call Vim_Size(2)
			let s:vim_size_select = 0
		endif
	endfunction
	function! Vim_Smart_Size_Select()
		if !exists("s:vim_smart_size_select")
			let s:vim_smart_size_select = 1
		endif
		if s:vim_smart_size_select == 0
			let s:vim_smart_size_select = 1
			let g:enable_vim_wm_smartsize = 1
			echo 'Smartsize = Enable'
		elseif s:vim_smart_size_select == 1
			let s:vim_smart_size_select = 0
			let g:enable_vim_wm_smartsize = 0
			echo 'Smartsize = Disable'
		endif
	endfunction
	function! Vim_Taskbar_Select()
		if !exists("s:vim_taskbar_select")
			let s:vim_taskbar_select = 1
		endif
		if s:vim_taskbar_select == 0
			let s:vim_taskbar_select = 1
			let g:enable_vim_wm_taskbar = 1
			echo 'Taskbar = Enable'
		elseif s:vim_taskbar_select == 1
			let s:vim_taskbar_select = 0
			let g:enable_vim_wm_taskbar = 0
			echo 'Taskbar = Disable'
		endif
	endfunction
	if exists("g:enable_vim_wm_defaulthotkey") &&
	 \ g:enable_vim_wm_defaulthotkey == 1
		nnoremap <F5> :call Vim_Pos()<CR>
		nnoremap <S-F5> :call Vim_Taskbar_Select()<CR>
		nnoremap <F6> :call Vim_Size_Select()<CR>
		nnoremap <S-F6> :call Vim_Smart_Size_Select()<CR>
	endif
	if !exists("g:enable_vim_wm_smartsize")
		let g:enable_vim_wm_smartsize = 1
	endif
	if !exists("g:enable_vim_wm_taskbar")
		let g:enable_vim_wm_taskbar = 1
	endif
	if !exists("g:vim_wm_big")
		let g:vim_wm_big = [1024 , 768]
	endif
	if !exists("g:vim_wm_large")
		let g:vim_wm_large = [1280 , 960]
	endif
endif
