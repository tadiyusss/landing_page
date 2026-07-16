function chatWidget() {
	return {
		open: true,
		hasOpened: false,
		typing: false,
		unread: 1,
		draft: '',
		show_input: false,
		messages: [],
		init() {
			// nothing here
		},
		scrollToBottom() {
			this.$nextTick(() => {
				const el = this.$refs.scrollArea;
				el.scrollTop = el.scrollHeight;
			});
		},
		toggle() {
			this.open ? this.close() : this.openChat();
		},
		openChat() {
			this.open = true;
			this.unread = 0;
			if (!this.hasOpened) {
				this.hasOpened = true;
				setTimeout(() => {
					this.messages.push({
						from: 'bot',
						text: "Hi there 👋 How can we help you today?"
					});
					this.scrollToBottom();
				}, 300);
			}
			this.$nextTick(() => this.$refs.input.focus());
		},
		close() {
			this.open = false;
		},
		autoGrow() {
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
			this.scrollToBottom();
			this.botReply(text);
		},

		botReply(userText) {
			this.typing = true;
			this.scrollToBottom();
			setTimeout(() => {
				this.typing = false;
				this.messages.push({
					from: 'bot',
					text: "Thanks for your message! A member of our team will be with you shortly."
				});
				this.scrollToBottom();
			}, 1100);
		}
	};
}