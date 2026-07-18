function chatWidget() {
	return {
		open: true,
		hasOpened: false,
		session_id: localStorage.getItem('chat_session_id') || '',
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
		socket: io(),
		init() {
			this.socket.on('connect', () => {
				if (this.session_id) {
					this.socket.emit('join', { session_id: this.session_id });
				}
			});
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
			if (!this.hasOpened) {
				this.hasOpened = true;
				setTimeout(() => {
					this.messages.push({
						from: 'bot',
						text: "Hi there 👋 How can we help you today?"
					});
					this.scroll_to_bottom();
				}, 300);
			}
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
			this.messages.push({
				from: 'user',
				text
			});
			this.draft = '';
			this.$nextTick(() => {
				this.$refs.input.style.height = 'auto';
			});
			this.scroll_to_bottom();
			this.bot_reply(text);
		},

		bot_reply(userText) {
			this.typing = true;
			this.scroll_to_bottom();
			setTimeout(() => {
				this.typing = false;
				this.messages.push({
					from: 'bot',
					text: "Thanks for your message! A member of our team will be with you shortly."
				});
				this.scroll_to_bottom();
			}, 1100);
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
					this.session_id = data.session_id;
					localStorage.setItem('chat_session_id', this.session_id);
				}
			})
			
		}
	};
}