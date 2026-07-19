function chatWidget() {
	return {
		open: true,
		hasOpened: false,
		session_id: localStorage.getItem('user_id') || '',
		typing: false,
		unread: 1,
		draft: '',
		messages: [],
		submitting: false,
		first_name: '',
		last_name: '',
		email: '',
		phone_number: '',
		errors: {},
		socket: null,
		init() {
			this.socket = io();

			this.socket.on('history', (data) => {
				this.messages = data.messages;
				this.scroll_to_bottom();
			});
			
			this.socket.emit('history', { 'user_id': this.session_id });
		},
		scroll_to_bottom() {
			this.$nextTick(() => {
				const el = this.$refs.scrollArea;
				el.scrollTop = el.scrollHeight;
			});
		},
		toggle() {
			this.open ? this.close() : this.open_chat();
		},
		open_chat() {
			this.open = true;
			this.unread = 0;
			this.$nextTick(() => this.$refs.input.focus());
		},
		close() {
			this.open = false;
		},
		auto_grow() {
			const el = this.$refs.input;
			el.style.height = 'auto';
			el.style.height = Math.min(el.scrollHeight, 96) + 'px';
		},
		send() {
			const text = this.draft.trim();
			if (!text) return;
			this.socket.emit('message', {
				'user_id': this.session_id,
				'message': text
			})
			this.message.push({
				'sender': 'client',
				'message_type': 'text',
				'content': text,
				'timestamp': new Date().toISOString()
			})
			this.draft = '';
			this.$nextTick(() => {
				this.$refs.input.style.height = 'auto';
			});
			this.scroll_to_bottom();
		},
		get allow_submit() {
			return !!(
				this.first_name.trim() &&
				this.last_name.trim() &&
				this.email.trim() &&
				this.phone_number.trim()
			);
		},
		submit_form(){
			if (!this.allow_submit) return;
			csrf_token = document.getElementById('csrf_token').value;
			fetch('/api/chat/start', {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
				},
				body: JSON.stringify({
					first_name: this.first_name,
					last_name: this.last_name,
					email: this.email,
					phone_number: this.phone_number,
					csrf_token: csrf_token
				})
			})
			.then(response => response.json())
			.then(data => {
				if (!data.success){
					this.errors = data.errors;
				} else {
					this.session_id = data.user_id;
					localStorage.setItem('user_id', this.session_id);
				}
			})
			
		}
	};
}