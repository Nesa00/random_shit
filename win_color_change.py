    def change_appearance_mode_event(self, new_appearance_mode):
        # print("pormena na ", new_appearance_mode)
        if(new_appearance_mode == "Light"):
            self.canvas.configure(bg='#ebebeb')
            # print("Light mode")
        elif(new_appearance_mode == "Dark"):
            self.canvas.configure(bg='#242424')
            # print("Dark mode")
        customtkinter.set_appearance_mode(new_appearance_mode)
